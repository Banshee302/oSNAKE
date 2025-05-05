import java.io.*;
import java.util.*;
import java.util.regex.*;

public class OSnakeParser {
    private static boolean verboseMode = false; 

    public static void main(String[] args) {
        System.out.println("oSNAKE Java Runtime Initialized...");

        
        if (args.length == 0) {
            System.out.println("Error: No script file specified.");
            System.out.println("Usage: java OSnakeParser [-v] <script-file>");
            return;
        }

        
        boolean verboseMode = false;
        String scriptFilePath;
        if (args.length > 1 && args[0].equals("-v")) {
            System.out.println("Verbose mode enabled.");
            verboseMode = true;
            scriptFilePath = args[1]; 
        } else {
            scriptFilePath = args[0]; 
        }

        File scriptFile = new File(scriptFilePath);
        if (!scriptFile.exists()) {
            System.out.println("Error: Script file not found.");
            return;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(scriptFile))) {
            StringBuilder script = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                script.append(line).append("\n");
            }
            System.out.println("Executing script: " + scriptFilePath);
            OSnakeParser parser = new OSnakeParser();
            parser.execute(script.toString(), verboseMode); 
        } catch (IOException e) {
            System.out.println("Error reading script file: " + e.getMessage());
        }
    }

    public void execute(String script, boolean verboseMode) {
        String[] lines = script.split("\n");
        for (String line : lines) {
            processLine(line.trim(), verboseMode);
        }
    }

    private void processLine(String line, boolean verboseMode) {
        if (verboseMode) System.out.println("Processing: " + line); 

        
        Pattern funcPattern = Pattern.compile("func\\{(\\w+)\\}");
        Matcher funcMatcher = funcPattern.matcher(line);
        if (funcMatcher.find()) {
            String funcName = funcMatcher.group(1);
            if (verboseMode) System.out.println("Defined function: " + funcName);
            return;
        }

        
        Pattern dataPattern = Pattern.compile("DATA\\[x=(\\d+)\\]");
        Matcher dataMatcher = dataPattern.matcher(line);
        if (dataMatcher.find()) {
            int value = Integer.parseInt(dataMatcher.group(1));
            if (verboseMode) System.out.println("Stored: DATA[x=" + value + "]");
            return;
        }

        
        Pattern tokenPrintPattern = Pattern.compile("print TOKEN\\[(\\w+)\\]");
        Matcher tokenPrintMatcher = tokenPrintPattern.matcher(line);
        if (tokenPrintMatcher.find()) {
            String tokenKey = tokenPrintMatcher.group(1);
            System.out.println(tokenKey);
            return;
        }

        
        Pattern printPattern = Pattern.compile("print\\s*\\((.*?)\\)");
        Matcher printMatcher = printPattern.matcher(line);
        if (printMatcher.find()) {
            System.out.println(printMatcher.group(1).trim()); 
        }
    }
}
