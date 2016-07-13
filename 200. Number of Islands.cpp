class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.size() == 0) return 0;
        int res = 0;
        vector <vector<bool>> visited (grid.size(), vector<bool> (grid[0].size(), false));
        for (int i = 0; i < grid.size(); i++)
        {
            for (int j = 0; j < grid[0].size(); j++)
            {
                if (!visited[i][j] && grid[i][j] == '1')
                {
                    count(i, j, grid, visited);
                    res ++;
                }
            }
        }
        return res;
    }
    void count(int i, int j, vector<vector<char>>& grid, vector<vector<bool>>& visited)
    {
        if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || visited[i][j] || grid[i][j] == '0')
            return;
        visited[i][j] = true;
        count(i-1, j, grid, visited);
        count(i+1, j, grid, visited);
        count(i, j-1, grid, visited);
        count(i, j+1, grid, visited);
    }
};
