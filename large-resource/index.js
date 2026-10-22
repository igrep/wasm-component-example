import { blobs, callGc, getGlobalContents } from "./out-python/python.js";

const blob = new blobs.Blob([1, 2, 3]);
blob.append(4);
callGc();
console.log("----");

console.log(blobs.Blob.getGlobalContents());
blob.appendGlobal(5);
callGc();
console.log("----");

console.log(getGlobalContents());
blob.appendGlobal(6);
callGc();
console.log("----");

console.log(blob.getContents());
