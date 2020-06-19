package nyobamaze;

import java.util.List;

/**
 *
 * @author Hann
 */
public class algo {
    
    public static boolean searchPath (int[][] maze, int x
            , int y, List<Integer> path){
    
        if (maze[y][x] == 9){
            path.add(x);
            path.add(y);
            return true;
        }
        
        if (maze[y][x] == 0){
            maze [y][x] = 2;
            
            int ax = -1;
            int ay = 0;
            if (searchPath(maze, x + ax, y + ay, path)){
                path.add(x);
                path.add(y);
                return true;
            }
            ax = 1;
            ay = 0;
            if (searchPath(maze, x + ax, y + ay, path)){
                path.add(x);
                path.add(y);
                return true;
            }
            ax = 0;
            ay = -1;
            if (searchPath(maze, x + ax, y + ay, path)){
                path.add(x);
                path.add(y);
                return true;
            }
            ax = 0;
            ay = 1;
            if (searchPath(maze, x + ax, y + ay, path)){
                path.add(x);
                path.add(y);
                return true;
            }                    
        }
        
        return false;
    }
}
