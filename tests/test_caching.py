import json
from pathlib import Path

from sigstickers.caching import CACHE_DIR, create_converted, verify_converted

THISDIR = Path(__file__).resolve().parent


# just want files that exist here
file_exists = "pyproject.toml"
file_exists_2 = ".gitignore"

file_not_exists = "file/not/exists"


def test_verify_converted_v1() -> None:
	pack_name = "Test_Pack_v1"
	cache_file = CACHE_DIR / pack_name
	cache_data = {
		"info": {"swd": f"{THISDIR}/data"},
		"converted": {"converted": 10, "total": 10},
	}
	cache_file.write_text(json.dumps(cache_data))

	assert verify_converted(Path(pack_name))


def test_verify_converted_v1_not_exists() -> None:
	pack_name = "Test_Pack_v1_not_exists"
	cache_file = CACHE_DIR / pack_name
	cache_data = {
		"info": {"swd": file_not_exists},
		"converted": {"converted": 10, "total": 10},
	}
	cache_file.write_text(json.dumps(cache_data))

	assert not verify_converted(Path(pack_name))


def test_verify_converted_v2() -> None:
	pack_name = "Test_Pack_v2"
	cache_file = CACHE_DIR / pack_name
	cache_data = {
		"version": 2,
		"webp_files": [file_exists, file_exists_2],
		"converted_files": [[file_exists], [file_exists_2]],
	}
	cache_file.write_text(json.dumps(cache_data))

	assert verify_converted(Path(pack_name))


def test_verify_converted_v2_partial_convert() -> None:
	pack_name = "Test_Pack_v2_partial_convert"
	cache_file = CACHE_DIR / pack_name
	cache_data = {
		"version": 2,
		"webp_files": [file_exists, file_exists_2],
		"converted_files": [[file_exists]],
	}
	cache_file.write_text(json.dumps(cache_data))

	assert not verify_converted(Path(pack_name))


def test_verify_converted_v2_not_exists() -> None:
	pack_name = "Test_Pack_v2_not_exists"
	cache_file = CACHE_DIR / pack_name
	cache_data = {
		"version": 2,
		"webp_files": [file_exists, file_not_exists],
		"converted_files": [[file_exists], [file_exists_2]],
	}
	cache_file.write_text(json.dumps(cache_data))

	assert not verify_converted(Path(pack_name))


def test_create_converted() -> None:
	pack_name = "Test_Pack"
	cache_data = {"example_key": "example_value"}

	create_converted(Path(pack_name), cache_data)

	cache_file = CACHE_DIR / pack_name
	assert cache_file.exists()
	assert json.loads(cache_file.read_text()) == cache_data
