class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = path.split("/")
        print(folders)
        st = []
        for f in folders:
            if not f:
                continue
            if f == ".":
                continue
            if f == "..":
                if st:
                    st.pop()
            else:
                st.append(f)
        res = ""
        for s in st:
            res += "/" + s
        return res if st else "/"
        