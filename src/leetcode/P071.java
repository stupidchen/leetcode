/**
 * Created by mike on 3/25/18.
 */
public class P071 {
    public String simplifyPath(String path) {
        String[] dir = path.split("/");
        for (int i = 0; i < dir.length; i++) {
            if (dir[i].equals("")) {
                dir[i] = null;
                continue;
            }
            if (dir[i].equals("..")) {
                int j = i - 1;
                while (j >= 0 && dir[j] == null) j--;
                if (j >= 0) dir[j] = null;
                dir[i] = null;
                continue;
            }
            if (dir[i].equals(".")) dir[i] = null;
        }

        String ret = "", last = null;
        for (int i = 0; i < dir.length; i++)
            if (dir[i] != null) ret += "/" + dir[i];
        if (ret.length() == 0) ret = "/";

        return ret;
    }

    public static void main(String[] args) {
        P071 p = new P071();
        System.out.println(p.simplifyPath("/a/./b/../../c/"));
    }
}
