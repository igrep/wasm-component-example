let escape = null;

export const processor = {
  process(b) {
    escape = b;
    b.append(100);
  },

  later() {
    escape.append(101);
    return escape.getContents();
  },
};
