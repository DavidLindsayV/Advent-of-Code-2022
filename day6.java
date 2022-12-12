import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Set;
import java.util.Stack;

class day6 {

  public static void main(String[] args) throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("practice.txt"));
    int myCount = 0;
    String line = lines.get(0);
    Map<Character, Integer> chars = new HashMap<Character, Integer>();
    int uniqueCharCount = 0;
    for (int i = 0; i < line.length(); i++) {
      if (i >= 14) {
        chars.put(line.charAt(i - 14), chars.get(line.charAt(i - 14)) - 1);
        if (chars.get(line.charAt(i - 14)) == 0) {
          uniqueCharCount--;
        }
      }
      if (chars.get(line.charAt(i)) == null) {
        chars.put(line.charAt(i), 0);
      }
      chars.put(line.charAt(i), chars.get(line.charAt(i)) + 1);
      if (chars.get(line.charAt(i)) == 1) {
        uniqueCharCount++;
      }
      if (uniqueCharCount == 14) {
        myCount = i + 1;
        break;
      }
    }
    System.out.println(myCount);
  }

  public static void part1() throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("input.txt"));
    String myResult = "";
    List<Stack<Character>> stacks = new ArrayList<Stack<Character>>();
    String line1 = lines.get(0);
    int numStacks = (line1.length() + 1) / 4;
    for (int i = 0; i < numStacks; i++) {
      stacks.add(new Stack<Character>());
    }
    //System.out.println("numStacks = " + numStacks);
    int endOfStacks = 0;
    for (int i = 0; i < lines.size(); i++) {
      String line = lines.get(i);
      if (!line.contains("[")) {
        endOfStacks = i + 2;
        break;
      }
      int charNum = 1;
      for (int j = 0; j < numStacks; j++) {
        if (line.charAt(charNum) != ' ') {
          stacks.get((charNum - 1) / 4).push(line.charAt(charNum));
        }
        charNum += 4;
      }
      System.out.println(stacks);
    }
    for (int i = 0; i < stacks.size(); i++) {
      Stack<Character> newStack = new Stack<>();
      while (stacks.get(i).size() != 0) {
        newStack.push(stacks.get(i).pop());
      }
      stacks.set(i, newStack);
    }
    for (int i = endOfStacks; i < lines.size(); i++) {
      //System.out.println(stacks);
      String line = lines.get(i);
      Scanner sc = new Scanner(line);
      //System.out.println(line);
      sc.next();
      int numMoved = sc.nextInt();
      sc.next();
      int fromIndex = sc.nextInt();
      sc.next();
      int toIndex = sc.nextInt();
      for (int j = 0; j < numMoved; j++) {
        Character c = stacks.get(fromIndex - 1).pop();
        stacks.get(toIndex - 1).push(c);
      }
    }
    for (int i = 0; i < numStacks; i++) {
      myResult += stacks.get(i).pop();
    }
    System.out.println(myResult);
  }
}
