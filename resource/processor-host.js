import { blobs } from "./out-python/python.js";
import { processor } from "./out-processor/processor.js";

const blob = new blobs.Blob([1, 2, 3]);
processor.process(blob);
console.log(blob.getContents());
console.log("----");

console.log(processor.later());
