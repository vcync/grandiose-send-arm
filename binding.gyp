{
    "variables": {
      "ndi_dir": "<(module_root_dir)/ndi"
    },
    "targets": [ {
        "target_name": "grandiose",
        "sources": [
            "src/grandiose_util.cc",
            "src/grandiose_find.cc",
            "src/grandiose_send.cc",
            "src/grandiose_receive.cc",
            "src/grandiose.cc"
        ],
        "include_dirs": [ "ndi/include" ],
        "conditions":[
            [ "OS == 'win' and target_arch == 'ia32'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "<(ndi_dir)/lib/win-x86/Processing.NDI.Lib.x86.dll" ]
                } ],
                "link_settings": {
                    "libraries":    [ "Processing.NDI.Lib.x86.lib" ],
                    "library_dirs": [ "<(ndi_dir)/lib/win-x86" ]
                }
            } ],
            [ "OS == 'win' and target_arch == 'x64'", {
                "copies": [ {
                    "destination":  "build/Release",
                    "files":        [ "<(ndi_dir)/lib/win-x64/Processing.NDI.Lib.x64.dll" ]
                } ],
                "link_settings": {
                    "libraries":    [ "Processing.NDI.Lib.x64.lib" ],
                    "library_dirs": [ "<(ndi_dir)/lib/win-x64" ]
                }
            } ],
            [ "OS == 'linux' and target_arch == 'ia32'", {
                "link_settings": {
                    "libraries":    [ "-Wl,-rpath,<(ndi_dir)/lib/lnx-x86", "-lndi" ],
                    "library_dirs": [ "<(ndi_dir)/lib/lnx-x86" ]
                }
            } ],
            [ "OS == 'linux' and target_arch == 'x64'", {
                "link_settings": {
                    "libraries":    [ "-Wl,-rpath,<(ndi_dir)/lib/lnx-x64", "-lndi" ],
                    "library_dirs": [ "<(ndi_dir)/lib/lnx-x64" ]
                }
            } ],
            [ "OS == 'mac' and target_arch == 'x64'", {
                "link_settings": {
                    "libraries":    [ "-Wl,-rpath,<(ndi_dir)/lib/mac-x64", "-lndi.4" ]
                    "library_dirs": [ "<(ndi_dir)/lib/max-x64" ]
                }
            } ]
        ]
    } ]
}
