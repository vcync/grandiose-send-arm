{
  "variables": {
    "ndi_dir": "<(module_root_dir)/ndi"
  },
  "targets": [
    {
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
        ["OS=='win'", {
          "copies":[
            {
              "destination": "build/Release",
              "files": [
                "ndi/lib/win-x64/Processing.NDI.Lib.x64.dll"
              ]
            }
          ],
          "link_settings": {
            "libraries": [ "Processing.NDI.Lib.x64.lib" ],
            "library_dirs": [ "ndi/lib/win-x64" ]
          },
        }],
        ["OS=='linux'", {
          'link_settings': {
              'libraries': [ "-L<(ndi_dir)/lib/lnx-x64", "-Wl,-rpath,<(ndi_dir)/lib/lnx-x64", "-lndi" ],
          }
        }],
        ["OS=='mac'", {
          'link_settings': {
              'libraries': [ "-L<(ndi_dir)/lib/mac-x64", "-Wl,-rpath,<(ndi_dir)/lib/mac-x64", "-lndi.4" ],
          }
        }]
      ]
    }
  ]
}
