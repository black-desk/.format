# ----------------------------------
# Options affecting listfile parsing
# ----------------------------------
with section("parse"):
    # Specify structure for custom cmake functions
    additional_commands = {
        "cpmaddpackage": {
            "kwargs": {
                "DOWNLOAD_COMMAND": 1,
                "DOWNLOAD_NAME": 1,
                "DOWNLOAD_NO_EXTRACT": 1,
                "DOWNLOAD_ONLY": 1,
                "EXCLUDE_FROM_ALL": 1,
                "FIND_PACKAGE_ARGUMENTS": 1,
                "FORCE": 1,
                "GITHUB_REPOSITORY": 1,
                "GITLAB_REPOSITORY": 1,
                "GIT_REPOSITORY": 1,
                "GIT_SHALLOW": 1,
                "GIT_TAG": 1,
                "HTTP_PASSWORD": 1,
                "HTTP_USERNAME": 1,
                "NAME": 1,
                "NO_CACHE": 1,
                "OPTIONS": "+",
                "SOURCE_DIR": 1,
                "SOURCE_SUBDIR": 1,
                "SVN_REPOSITORY": 1,
                "SVN_REVISION": 1,
                "URL": 1,
                "URL_HASH": 1,
                "URL_MD5": 1,
                "VERSION": 1,
            },
            "pargs": {"flags": [], "nargs": "*"},
            "spelling": "CPMAddPackage",
        },
        "cpmdeclarepackage": {
            "kwargs": {
                "DOWNLOAD_COMMAND": 1,
                "DOWNLOAD_NAME": 1,
                "DOWNLOAD_NO_EXTRACT": 1,
                "DOWNLOAD_ONLY": 1,
                "EXCLUDE_FROM_ALL": 1,
                "FIND_PACKAGE_ARGUMENTS": 1,
                "FORCE": 1,
                "GITHUB_REPOSITORY": 1,
                "GITLAB_REPOSITORY": 1,
                "GIT_REPOSITORY": 1,
                "GIT_SHALLOW": 1,
                "GIT_TAG": 1,
                "HTTP_PASSWORD": 1,
                "HTTP_USERNAME": 1,
                "NAME": 1,
                "NO_CACHE": 1,
                "OPTIONS": "+",
                "SOURCE_DIR": 1,
                "SOURCE_SUBDIR": 1,
                "SVN_REPOSITORY": 1,
                "SVN_REVISION": 1,
                "URL": 1,
                "URL_HASH": 1,
                "URL_MD5": 1,
                "VERSION": 1,
            },
            "pargs": {"flags": [], "nargs": "*"},
            "spelling": "CPMDeclarePackage",
        },
        "cpmfindpackage": {
            "kwargs": {
                "DOWNLOAD_COMMAND": 1,
                "DOWNLOAD_NAME": 1,
                "DOWNLOAD_NO_EXTRACT": 1,
                "DOWNLOAD_ONLY": 1,
                "EXCLUDE_FROM_ALL": 1,
                "FIND_PACKAGE_ARGUMENTS": 1,
                "FORCE": 1,
                "GITHUB_REPOSITORY": 1,
                "GITLAB_REPOSITORY": 1,
                "GIT_REPOSITORY": 1,
                "GIT_SHALLOW": 1,
                "GIT_TAG": 1,
                "HTTP_PASSWORD": 1,
                "HTTP_USERNAME": 1,
                "NAME": 1,
                "NO_CACHE": 1,
                "OPTIONS": "+",
                "SOURCE_DIR": 1,
                "SOURCE_SUBDIR": 1,
                "SVN_REPOSITORY": 1,
                "SVN_REVISION": 1,
                "URL": 1,
                "URL_HASH": 1,
                "URL_MD5": 1,
                "VERSION": 1,
            },
            "pargs": {"flags": [], "nargs": "*"},
            "spelling": "CPMFindPackage",
        },
        "cpmgetpackageversion": {"pargs": 2, "spelling": "CPMGetPackageVersion"},
        "cpmregisterpackage": {"pargs": 1, "spelling": "CPMRegisterPackage"},
        "cpmusepackagelock": {"pargs": 1, "spelling": "CPMUsePackageLock"},
        "packageproject": {
            "kwargs": {
                "BINARY_DIR": 1,
                "COMPATIBILITY": 1,
                "DEPENDENCIES": "+",
                "INCLUDE_DESTINATION": 1,
                "INCLUDE_DIR": 1,
                "NAME": 1,
                "VERSION": 1,
                "VERSION_HEADER": 1,
            },
            "pargs": {"flags": [], "nargs": "*"},
            "spelling": "packageProject",
        },
        "target_compile_features": {
            "kwargs": {"INTERFACE": "+", "PRIVATE": "+", "PUBLIC": "+"},
            "pargs": 1,
        },
        "target_include_directories": {
            "flags": ["SYSTEM", "BEFORE", "AFTER"],
            "kwargs": {"INTERFACE": "+", "PRIVATE": "+", "PUBLIC": "+"},
            "pargs": 1,
        },
        "target_link_libraries": {
            "kwargs": {"INTERFACE": "+", "PRIVATE": "+", "PUBLIC": "+"},
            "pargs": 1,
        },
        "target_sources": {
            "kwargs": {"INTERFACE": "+", "PRIVATE": "+", "PUBLIC": "+"},
            "pargs": 1,
        },
        "find_package": {
            "kwargs": {"NAMES": "+", "COMPONENTS": "+", "ORIGINAL_COMPONENTS": "+"},
            "flags": [
                "REQUIRED",
                "EXACT",
                "QUITE",
                "MODULE",
                "GLOBAL",
                "NO_POLICY_SCOPE",
                "BYPASS_PROVIDER",
            ],
        },
        "set_source_files_properties": {
            "kwargs": {"PROPERTIES": "+", "DIRECTORY": "+", "TARGET_DIRECTORY": "+"},
            "pargs": "*",
        },
    }


# -----------------------------
# Options affecting formatting.
# -----------------------------
with section("format"):
    # How wide to allow formatted cmake files
    line_width = 80

    # How many spaces to tab for indent
    tab_size = 8

    # If an argument group contains more than this many sub-groups (parg or kwarg
    # groups) then force it to a vertical layout.
    max_subgroups_hwrap = 2

    # If a statement is wrapped to more than one line, than dangle the closing
    # parenthesis on its own line.
    dangle_parens = True

    # If the statement spelling length (including space and parenthesis) is larger
    # than the tab width by more than this amount, then force reject un-nested
    # layouts.
    max_prefix_chars = 0
    max_pargs_hwrap = 3

    # If a candidate layout is wrapped horizontally but it exceeds this many
    # lines, then reject the layout.
    max_lines_hwrap = 1

    # A dictionary mapping layout nodes to a list of wrap decisions. See the
    # documentation for more information.
    layout_passes = {"KwargGroupNode": [(0, True)]}

    separate_fn_name_with_space = (True,)

    always_wrap = [
        "project",
        "find_package",
        "target_sources",
        "target_link_libraries",
        "target_include_directories",
        "set_source_files_properties",
    ]
