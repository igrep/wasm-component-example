import { blobs } from "./out-python/python.js";

const blob = new blobs.Blob([1, 2, 3]);
blob.append(4);
blob.append(5);

console.log(blob.getContents());
