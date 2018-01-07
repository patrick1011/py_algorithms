
import java.util.ArrayList;

class anti_diagonals {
	public static void main(String args[]) {
		Integer n = 3;

		int[][] grid = new int[][]{
			{1, 2, 3},
			{4, 5, 6},
			{7, 8, 9}
		};

		ArrayList<ArrayList<Integer>> output = new ArrayList<ArrayList<Integer>>();

		for (int i=0; i<n*n; i++) {
			output.add(new ArrayList<Integer>());
		}


		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				output.get(i + j).add(grid[i][j]);
			}
		}
	}
}