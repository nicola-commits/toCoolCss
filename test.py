from unwrap import unwrapCSS as u
from unwrap import unwrapJS as j
from unwrap import wrap
if __name__ == "__main__":
    # u("test/test0.css", result="test/test0.txt")
    # u("test/test1.css", result="test/test1.txt")
    # u("test/test2.css", result="test/test2.txt")
    # u("test/test3.css", result="test/test3.txt")
    j(wrap("test/test0.js"), result="test/test0.txt", text=True)