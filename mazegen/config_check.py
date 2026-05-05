from pathlib import Path
from typing_extensions import Self, Optional, Any
from pydantic import ValidationError, BaseModel, Field, model_validator


class Config(BaseModel):
    width: int = Field(ge=1, le=40)
    height: int = Field(ge=1, le=40)
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: Optional[int] = None

    @model_validator(mode="after")
    def validate_coords(self) -> Self:
        if self.entry[0] == self.exit[0] and self.entry[1] == self.exit[1]:
            raise ValueError("Entry cannot be equal to exit")
        if self.entry[0] < 0 or self.entry[0] >= self.width:
            raise ValueError("Entry_x must be in range(0,'width')")
        if self.entry[1] < 0 or self.entry[1] >= self.height:
            raise ValueError("Entry_y must be in range(0,'height')")
        if self.exit[0] < 0 or self.exit[0] >= self.width:
            raise ValueError("Exit_x must be in range(0,'width')")
        if self.exit[1] < 0 or self.exit[1] >= self.height:
            raise ValueError("Exit_y must be in range(0,'height')")
        return self


def get_key_val(
        line: str,
        valid_config_keys: list[str]) -> tuple[str, str] | None:
    key_value = line.split("=")
    key_value[0] = key_value[0].lower()
    if len(key_value) == 2 and key_value[0] in valid_config_keys:
        return (key_value[0], key_value[1])
    return None


def clean_empty(
        my_list: list[tuple[str, str] | None]
        ) -> list[tuple[str, str]]:
    return [d for d in my_list if d]


def unify_list(key_value_list: list[tuple[str, str]]) -> dict[str, Any]:
    my_dict: dict[str, Any] = {}
    for key, value in key_value_list:
        if not value:
            my_dict[key] = None
        elif key == "entry" or key == "exit":
            my_dict[key] = tuple(value.split(","))
        else:
            my_dict[key] = value
    return my_dict


def validate_config(file_path: Path, key_value: dict[str, Any]) -> Config:
    try:
        return Config(**key_value)
    except ValidationError as e:
        for error in e.errors():
            print(f"Error for {error['loc']}: {error['msg']}")
        raise ValueError(f"{file_path} file has incorrect format")


def get_config(file_path: Path) -> Config:
    valid_config_keys = [
        "width",
        "height",
        "entry",
        "exit",
        "output_file",
        "perfect",
        "seed"
    ]
    with file_path.open("r") as file:
        lines = file.read().splitlines()
    key_value_list: list[tuple[str, str] | None] = []
    for line in lines:
        if line and line[0] != "#" and "=" in line:
            key_value_list.append(get_key_val(line, valid_config_keys))
    key_value = unify_list(clean_empty(key_value_list))
    return validate_config(file_path, key_value)
