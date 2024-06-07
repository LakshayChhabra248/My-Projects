const fs = require("fs")
const path = require("path")
const dirtoOrganize = "./Sample Directory"
function clearDirectory(dirName){
    fs.readdir(dirName, (err, files) => {
        if (err) {
            throw err
        }
        for (const file of files) {
            const fPath = path.join(dirName, file)
            fs.stat(fPath, (err, stats) => {
                if (err) {
                    throw err
                }
                if (stats.isFile()){
                    const fExt = path.extname(fPath)
                    const extName = fExt.slice(1)
                    const newDirPath = path.join(dirName, extName)
                    fs.mkdirSync(newDirPath, {recursive: true})
                    const newFilePath = path.join(newDirPath, file)
                    fs.renameSync(fPath, newFilePath)
                }
            })
        }
    })
}
clearDirectory(dirtoOrganize)
console.log("Decluttering Completed ✅")
