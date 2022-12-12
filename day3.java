import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;

class day3 {

  public static void main(String[] args) throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("input.txt"));
    int myScore = 0;
    for (int i = 0; i < lines.size(); i++) {
      String line1 = lines.get(i);
      String line2 = lines.get(i + 1);
      String line3 = lines.get(i + 2);
      i += 2;
      Set<Character> set = new HashSet<Character>();
      for (Character c : line1.toCharArray()) {
        set.add(c);
      }
      Set<Character> set2 = new HashSet<Character>();
      for (char c : line2.toCharArray()) {
        set2.add(c);
      }
      Set<Character> set3 = new HashSet<Character>();
      for (char c : line3.toCharArray()) {
        set3.add(c);
      }
      set.retainAll(set2);
      set.retainAll(set3);
      for (Character c : set) {
        myScore += charToNum(c);
      }
    }
    System.out.println(myScore);
  }

  static void part1() throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("input.txt"));
    int myScore = 0;
    for (String s : lines) {
      String firstHalf = s.substring(0, s.length() / 2);
      String secondHalf = s.substring(s.length() / 2, s.length());
      Set<Character> set = new HashSet<Character>();
      for (char c : firstHalf.toCharArray()) {
        set.add(c);
      }
      for (char c : secondHalf.toCharArray()) {
        if (set.contains(c)) {
          myScore += charToNum(c);
          break;
        }
      }
    }
    System.out.println(myScore);
  }

  static int charToNum(Character c) {
    return (
      Character.getNumericValue(c) + (Character.isUpperCase(c) ? 26 : 0) - 9
    );
  }
}
