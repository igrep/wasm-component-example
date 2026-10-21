import { blobs, callGc } from "./out-python/python.js";

callGc();
const blob = new blobs.Blob([1, 2, 3]);
blob.append(4);
callGc();
console.log(blob.getContents());
blob.appendGlobal(5);
callGc();

console.log(blob.getContents());
