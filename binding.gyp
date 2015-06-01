{
    "targets": [
        {
            "target_name": "gsl",
            "sources": [ "gsl.cc", "random.cc", "statistics.cc" ],
            "dependencies": ["gsl-lib"],
            "include_dirs" : [
 	 			"<!(node -e \"require('nan')\")"
			]
        },

        {
            "target_name": "gsl-lib",
            "sources": [ "deps/gsl-1.14/configure" ],
            "type": "none",
            "dependencies": [],
            "actions": [
                {
                    "action_name": "build-gsl-lib",
                    "message":     "building gsl-lib...",
                    "inputs":      ["deps/gsl-1.14/configure"],
                    "outputs":     ["deps/gsl-1.14/config.h"],
                    "action": [
                        "sh",
                        "-c",
                        "mkdir -p deps-build && rm -rf deps-build/* && cp -rp deps/gsl-1.14/ deps-build && cd deps-build && chmod u+x ./configure && ./configure --disable-shared && make"
                    ],
                }
            ]
        },

    ]
}
