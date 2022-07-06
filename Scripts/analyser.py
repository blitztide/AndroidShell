import zipfile
import axmldecode
import hashlib

def do_analysis(args):
    if not len(args) == 3:
        raise("ERR_ARGS")
    repo,package,version = args
    apk = get_apk_handle(repo,package,version)
    get_file_hashes(apk)
    if zipfile.is_zipfile(apk):
        archive = zipfile.ZipFile(apk)
        manifest = archive.open("AndroidManifest.xml")
        decoder = axmldecode.AndroidXMLDecompress()
        print(decoder.decompressXML(manifest.read()))
    else:
        raise("not zipfile")
    close_apk_handle(apk)


def get_apk_handle(repo,package,version):
    file_path = "/UNI/db/{}/{}_{}.apk".format(repo,package,version)
    apk = open(file_path,"rb")
    return apk

def close_apk_handle(apk):
    apk.close()

def get_file_hashes(handle):
    fullfile = handle.read()

    md5Hash = hashlib.md5(fullfile)
    md5sum = md5Hash.hexdigest()

    sha1Hash = hashlib.sha1(fullfile)
    sha1sum = sha1Hash.hexdigest()

    print("md5sum:",md5sum)
    print("sha1sum:",sha1sum)
