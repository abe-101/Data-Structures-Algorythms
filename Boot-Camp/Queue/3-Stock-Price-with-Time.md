---
title: 3-Stock-Price-with-Time
updated: 2022-04-01 17:30:19Z
created: 2022-03-28 15:09:39Z
tags:
  - medium
  - queue
---

## **Stock Price with Time**

<ins>**Level**: Medium</ins>
You are given stock prices and the corresponding day of each stock price.
For example:
(32, 1), (45, 1), (37,2), (42,3), ..
Here, 32 is the price and 1 is the day of the price.
Say you are given these prices as an input stream. You should provide a function for the user to input a stock price and day. Your system should be able to tell
the maximum stock price in the last 3 days.

Questions to Clarify:
Q. Can the user add a new stock price anytime?
A. Yes, the user can add a new price anytime using your function

Q. Can we assume that the user will provide the stock price for today?
i.e, will the stock prices be sorted by day?
A. Yes, you can assume that.

Q. Let’s say we get a price on day 4. Should the window be of prices o day 2,3 and 4?
A. Yes

Q. If there is no price in the system, what should the max() function return?
A. Return 0.

## Solution

We maintain a sliding window, where each price in the window is within the last 3 days.
Every time a new stock price comes in, we add it to the sliding window and remove
all elements that exceed 3 days from the back.

**Pseudocode**:

```
addPrice(price, day)
    while back of queue is less than day-2
        remove the front of the queue
    add (price, day) to queue

getMax()
    find max of the queue by going through it.
```

<ins>Test Cases:</ins>
Edge Cases: empty price, empty day
Base Cases: empty queue, 1 item in queue
Regular Cases: no element in past 3 days, adding on new day

Time Complexity:
addPrice()​- O(n) worst case, but O(1) amortized because we do N removals for N insertions
findMax()​ - O(n) because we go through entire sliding window. We can reduce this to O(1) by
maintaining a ​Queue with Max​, which we cover in the next section.
Space Complexity:​ O(n)

**code:**

```java
public class StockPriceWithTime {
    Queue<Price> q;
    int window;
    
    public StockPriceWithTime(int windowDays) {
        q = new LinkedList<>();
        window = windowDays;
    }
    
    public void addPrice(int price, int day) {
        while(!q.isEmpty() && q.peek().getDay() < (day - window + 1))
            q.remove();
        
        w.add(new Price(pricem day))
    }
    
    // Returns max price in the last 3 days
    public int getMax() {
        int maxPrice = 0;
        Iterator<Price> iter = q.iterator();
        while (iter.hasNext()) {
            int price = ((price) iter.next()).getPrice();
            if (price > maxPrice)
                maxPrice = price;
        }
        return maxPrice
    }
}

// Helper Code
public class Price {
    int price;
    int day;
    
    public Price(int price, int day) {
        this.price = price;
        this.day = day;
    }
    
    public int getPrice() {
        return price;
    }
    
    public int getDay() {
        return day;
    }
}
```