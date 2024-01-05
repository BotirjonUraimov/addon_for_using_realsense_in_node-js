{
  "targets": [
    {
      "target_name": "cinet",
      "sources": [ "addon.cpp" ],
      "include_dirs": [
        "C:/Program Files (x86)/Intel RealSense SDK 2.0/include", 
        "C:/Program Files (x86)/Intel RealSense SDK 2.0/include/librealsense2",
        "<!@(node -p \"require('node-addon-api').include\")"  
      ],
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "conditions": [
        ["OS=='win'", {
          "defines": [ "_ENABLE_EXTENDED_ALIGNED_STORAGE" ], 
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1,  
              "EnableAsyncExceptionHandling": 1 
            }
          }
        }]
      ],
      "libraries": [
  
        "C:/Program Files (x86)/Intel RealSense SDK 2.0/lib/x64/realsense2.lib",
      ],
       "defines": [ "NAPI_DISABLE_CPP_EXCEPTIONS" ],
    }
  ]
}
