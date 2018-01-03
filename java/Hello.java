// Given a collection of intervals, merge all overlapping intervals.

// For example:

// Given [1,3],[2,6],[8,10],[15,18],

// return [1,6],[8,10],[15,18].

// Make sure the returned intervals are sorted.

import java.util.ArrayList;
import java.util.Iterator;
import java.util.Collection;
import java.util.List;


class Interval {
	int start;
	int end;
	Interval() { start = 0; end = 0; }
	Interval(int s, int e) { start = s; end = e; }

}

class Hello {
    public static void main(String args[]) {

    	Collection<Interval> intervals = new ArrayList<Interval>();

    	intervals.add(new Interval(3, 5));
    	intervals.add(new Interval(1, 3));
    	intervals.add(new Interval(5, 7));
    	intervals.add(new Interval(2, 5));
    	intervals.add(new Interval(5, 9));
    	intervals.add(new Interval(13, 20));

    	// Iterator<Interval> iterator = intervals.iterator(); 

    	// // 4 ways to loop through a collection
    	// System.out.println("Print using while loop:");
    	// while (iterator.hasNext()) {
    	// 	Interval interval = iterator.next();
    	// 	System.out.format("s: %d e: %d \n", interval.start, interval.end);
    	// }

    	// // Need to cast intervals as List to get indexing.
    	// ArrayList<Interval> arrIntervals = (ArrayList<Interval>)intervals;
    	// System.out.println("Print using for loop:");
    	// for (int i = 0; i < arrIntervals.size(); i++) {
    	// 	int s = arrIntervals.get(i).start; 
    	// 	int e = arrIntervals.get(i).end;
    	// 	System.out.format("s: %d e: %d \n", s, e);
    	// }

    	// // Print using for loop with iterator
    	// System.out.println("Print using for loop with iterator:");
    	// for (iterator = intervals.iterator(); iterator.hasNext();) {
    	// 	Interval interval = iterator.next();
    	// 	System.out.format("s: %d e: %d \n", interval.start, interval.end);
    	// }

    	ArrayList<Interval> output = new ArrayList<Interval>();
    	Interval lastElement; Integer end;
    	for (Interval interval: intervals) {
    		lastElement = output.isEmpty() ? null : output.get(output.size() - 1);
    		if ((lastElement != null) && (interval.start < lastElement.end)) {
    			output.remove(output.size() - 1);
    			end = Math.max(lastElement.end, interval.end);
    			output.add(new Interval(lastElement.start, end));
    		} else {
    			output.add(interval);
    		}
    	}

    	Iterator<Interval> iterator = output.iterator(); 

     	while (iterator.hasNext()) {
    		Interval interval = iterator.next();
    		System.out.format("s: %d e: %d \n", interval.start, interval.end);
    	}



    }
}

 











