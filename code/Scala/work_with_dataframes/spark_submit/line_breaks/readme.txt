This project should be compiled into jar.
Steps to perform the compilation:
1. Install sbt (using Homebrew)
2. Create folder structure (check the example of current structure)
3. From project root folder (i.e from here) run the following commands:
   sbt compile
   sbt package
4. Run the following command:
   spark-submit --verbose --class "line_breaks" --master local[4] target/scala-2.11/line-breaks_2.11-1.0.jar