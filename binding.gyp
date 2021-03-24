{
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
          "copies":[
            {
              "destination": "build/Release",
              "files": [
                "ndi/lib/lnx-x64/libndi.so",
                "ndi/lib/lnx-x64/libndi.so.4",
                "ndi/lib/lnx-x64/libndi.so.4.6.2",
              ]
            }
          ],
        }],
        ["OS=='mac'", {
          "copies":[
            {
              "destination": "build/Release",
              "files": [
                "ndi/lib/mac-x64/libndi.4.dylib"
              ]
            }
          ],
        }]
      ]
    }
  ]
}
