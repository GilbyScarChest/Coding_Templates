package com.example.java;

public class Main {

    public static void main(String[] args) {

        try {
            String welcome = "Welcome!";
            char[] chars = welcome.toCharArray();
            char lastChar = chars[chars.length -1];
            System.out.println("Last char: " + lastChar);
        } catch (ArrayIndexOutOfBoundsException e) {
            e.printStackTrace();
            return;
        }
        System.out.println("Code ran successfully");
    }
}
