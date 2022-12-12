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

class day4 {

  public static void main(String[] args) throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("input.txt"));
    int myScore = 0;
    for (String s : lines) {
      Scanner sc = new Scanner(s);
      sc.useDelimiter(",");
      String elf1 = sc.next();
      String elf2 = sc.next();
      int elf1Min = Integer.parseInt(elf1.substring(0, elf1.indexOf("-")));
      int elf1Max = Integer.parseInt(
        elf1.substring(elf1.indexOf("-") + 1, elf1.length())
      );
      int elf2Min = Integer.parseInt(elf2.substring(0, elf2.indexOf("-")));
      int elf2Max = Integer.parseInt(
        elf2.substring(elf2.indexOf("-") + 1, elf2.length())
      );

      if (
        (elf1Max >= elf2Min && elf1Max <= elf2Max) ||
        (elf1Min >= elf2Min && elf1Min <= elf2Max) ||
        (elf2Max >= elf1Min && elf2Max <= elf1Max) ||
        (elf2Min >= elf1Min && elf2Min <= elf1Max)
      ) {
        myScore++;
      }
    }
    System.out.println(myScore);
  }

  static void part1() throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("input.txt"));
    int myScore = 0;
    for (String s : lines) {
      Scanner sc = new Scanner(s);
      sc.useDelimiter(",");
      String elf1 = sc.next();
      String elf2 = sc.next();
      int elf1Min = Integer.parseInt(elf1.substring(0, elf1.indexOf("-")));
      int elf1Max = Integer.parseInt(
        elf1.substring(elf1.indexOf("-") + 1, elf1.length())
      );
      int elf2Min = Integer.parseInt(elf2.substring(0, elf2.indexOf("-")));
      int elf2Max = Integer.parseInt(
        elf2.substring(elf2.indexOf("-") + 1, elf2.length())
      );

      if (
        (elf1Min <= elf2Min && elf1Max >= elf2Max) ||
        (elf2Min <= elf1Min && elf2Max >= elf1Max)
      ) {
        myScore++;
      }
    }
    System.out.println(myScore);
  }
}
