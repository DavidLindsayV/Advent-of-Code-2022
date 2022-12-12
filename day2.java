import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.PriorityQueue;
import java.util.Scanner;

class day2 {

  public static void main(String[] args) throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("input.txt"));
    int myScore = 0;
    for (String s : lines) {
      Scanner sc = new Scanner(s);
      String opponent = sc.next();
      String myPlay = sc.next();
      myScore += myScore(opponent, whatToPlay(opponent, myPlay));
    }
    System.out.println(myScore);
  }

  public static void part1() throws IOException {
    List<String> lines = Files.readAllLines(Paths.get("input.txt"));
    int myScore = 0;
    for (String s : lines) {
      Scanner sc = new Scanner(s);
      String opponent = sc.next();
      String myPlay = sc.next();
      myScore += myScore(opponent, myPlay);
    }
    System.out.println(myScore);
  }

  static String whatToPlay(String opponent, String myPlay) {
    int enemy = stringToInt(opponent);
    int me = 0;
    if (myPlay.equals("X")) {
      me = (enemy - 1);
      if (me == 0) {
        me += 3;
      }
    } else if (myPlay.equals("Y")) {
      me = enemy;
    } else {
      me = enemy + 1;
      if (me == 4) {
        me = 1;
      }
    }
    return intToChar(me);
  }

  static String intToChar(int x) {
    if (x == 1) {
      return "X";
    } else if (x == 2) {
      return "Y";
    } else {
      return "Z";
    }
  }

  static int stringToInt(String s) {
    if (s.equals("A")) {
      return 1;
    } else if (s.equals("B")) {
      return 2;
    } else {
      return 3;
    }
  }

  static int myScore(String opponent, String myPlay) {
    int enemy = 1;
    if (opponent.equals("B")) {
      enemy = 2;
    } else if (opponent.equals("C")) {
      enemy = 3;
    }
    int me = 1;
    if (myPlay.equals("Y")) {
      me = 2;
    } else if (myPlay.equals("Z")) {
      me = 3;
    }

    return (
      me +
      (enemy == me ? 3 : 0) +
      (me - enemy == 1 || me == 1 && enemy == 3 ? 6 : 0)
    );
  }
}
