import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

class day1 {

  public static void main(String[] args) throws IOException {
    PriorityQueue<Integer> pq = new PriorityQueue<Integer>((a, b) -> b - a);
    List<String> lines = Files.readAllLines(Paths.get("input.txt"));
    int currentCalories = 0;
    for (String s : lines) {
      if (!s.equals("")) {
        currentCalories += Integer.parseInt(s);
      } else {
        pq.add(currentCalories);
        currentCalories = 0;
      }
    }
    pq.add(currentCalories);

    System.out.println(pq.toString());
    System.out.println(pq.poll() + pq.poll() + pq.poll());
  }
}
