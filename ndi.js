
/*  external requirements  */
const fs        = require("fs")
const path      = require("path")
const os        = require("os")
const shell     = require("shelljs")
const execa     = require("execa")
const zip       = require("cross-zip")
const got       = require("got")
const mkdirp    = require("mkdirp")
const tmp       = require("tmp")

/*  establish asynchronous environment  */
;(async () => {
    if (os.platform() === "win32") {
        /*  download innoextract utility  */
        const url1 = "https://constexpr.org/innoextract/files/innoextract-1.9-windows.zip"
        console.log("-- downloading innoextract utility")
        const data1 = await got(url1, { responseType: "buffer" })
        const file1 = tmp.tmpNameSync()
        await fs.promises.writeFile(file1, data1.body, { encoding: null })

        /*  extract innoextract utility  */
        console.log("-- extracting innoextract utility")
        const dir1 = tmp.tmpNameSync()
        zip.unzipSync(file1, dir1)

        /*  download NDI SDK distribution  */
        const url2 = "https://downloads.ndi.tv/SDK/NDI_SDK/NDI 4 SDK.exe"
        console.log("-- dowloading NDI SDK distribution")
        const data2 = await got(url2, { responseType: "buffer" })
        const file2 = tmp.tmpNameSync()
        await fs.promises.writeFile(file2, data2.body, { encoding: null })

        /*  extract NDI SDK distribution  */
        console.log("-- extracting NDI SDK distribution")
        const dir2 = tmp.tmpNameSync()
        execa.sync(path.join(dir1, "innoextract.exe"), [ "-s", "-d", dir2, file2 ],
            { stdin: "inherit", stdout: "inherit", stderr: "inherit" })

        /*  assemble NDI SDK subset  */
        console.log("-- assembling NDI SDK subset")
        shell.rm("-rf", "ndi")
        shell.mkdir("-p", "ndi/include")
        shell.mkdir("-p", "ndi/lib")
        shell.cp(path.join(dir2, "app/Include/*.h"), "ndi/include/")
        shell.cp(path.join(dir2, "app/Lib/x86/Processing.NDI.Lib.x86.lib"), "ndi/lib/Processing.NDI.Lib.x86.lib")
        shell.cp(path.join(dir2, "app/Bin/x86/Processing.NDI.Lib.x86.dll"), "ndi/lib/Processing.NDI.Lib.x86.dll")
        shell.cp(path.join(dir2, "app/Lib/x64/Processing.NDI.Lib.x64.lib"), "ndi/lib/Processing.NDI.Lib.x64.lib")
        shell.cp(path.join(dir2, "app/Bin/x64/Processing.NDI.Lib.x64.dll"), "ndi/lib/Processing.NDI.Lib.x64.dll")

        /*  remove temporary files  */
        shell.rm("-f", file1)
        shell.rm("-f", file2)
        shell.rm("-rf", dir1)
        shell.rm("-rf", dir2)
    }
    else if (os.platform() === "darwin") {
    }
    else if (os.platform() === "linux") {
    }
})().catch((err) => {
    console.log(`** ERROR: ${err}`)
})

