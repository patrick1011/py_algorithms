// Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

// Example:

// Given n = 3,

// You should return the following matrix:

// [
//   [ 1, 2, 3 ],
//   [ 8, 9, 4 ],
//   [ 7, 6, 5 ]
// ]

import java.util.ArrayList;

class SpiralOrder2 {
	public static void main(String args[]) {

		ArrayList<ArrayList<Integer>> grid = new ArrayList<ArrayList<Integer>>();

		Integer n = 4;

		for (Integer i=0; i<n; i++) {
			ArrayList<Integer> row = new ArrayList<Integer>();
			for (Integer j=0; j<n; j++){
				row.add(0);
			}
			grid.add(row);
		}

		Integer i=0, j=0, di=0, dj=1, tempi=0;

		for (Integer k=1; k<=n*n; k++) {
			grid.get(i).set(j, k);
			if (grid.get(Math.abs((i + di) % n)).get(Math.abs((j + dj) % n)) != 0) {
				tempi = di; 
				di = dj;
				dj = -tempi;
			}
			i += di;
			j += dj;
		}

		for (i=0; i<n; i++) {
			for (j=0; j<n; j++){
				System.out.format("i=%d, j=%d, vak=%d \n", i, j, grid.get(i).get(j));
			}
		}

	}
}