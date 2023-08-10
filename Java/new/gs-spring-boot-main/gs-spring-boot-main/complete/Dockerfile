FROM maven:3.8-jdk-11 AS builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY src/ ./src/
RUN mvn package
FROM tomcat:9-jdk11
WORKDIR /usr/local/tomcat/webapps
COPY --from=builder /app/target/spring-boot-initial-0.0.1-SNAPSHOT.jar ./spring-boot-initial-0.0.1-SNAPSHOT.jar
EXPOSE 8080
CMD ["java", "-jar", "/usr/local/tomcat/webapps/spring-boot-initial-0.0.1-SNAPSHOT.jar"]