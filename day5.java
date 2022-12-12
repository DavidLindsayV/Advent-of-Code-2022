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

class day5 {

  public static void main(String[] args) throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("practice.txt"));
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
      Stack<Character> newStack = new Stack<Character>();
      for (int j = 0; j < numMoved; j++) {
        Character c = stacks.get(fromIndex - 1).pop();
        newStack.push(c);
      }
      for (int j = 0; j < numMoved; j++) {
        stacks.get(toIndex - 1).push(newStack.pop());
      }
    }
    for (int i = 0; i < numStacks; i++) {
      myResult += stacks.get(i).pop();
    }
    System.out.println(myResult);
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
