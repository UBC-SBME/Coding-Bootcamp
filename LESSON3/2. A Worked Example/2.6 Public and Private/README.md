# Do we Trust the User?

In this section User is simply whoever will use your code in there own programs. If someone make a class called “Owner” which uses your “MyPetDog” class, that someone is a user.
No. We do not trust the user. Assume the user is a malicious urchin, always. User trust is what inspired the `public` and `private` keywords. `public` and `private` are used to say if a user can freely access certain methods and variables.
Justification on whether to use `public` and `private` differ for both variables and methods, but both center around how much you trust the user. Let’s start with Variables.

## Why would you Make Instance Variable Public or Private?

Usually, it is because you want to prevent the user from doing something obscenely stupid. Let’s fall back to our `MyPetDog`. As we have it now, `age` is public. That means, our user can do something like this.
```java
MyPetDog x = new MyPetDog();
x.age = -99999;
```
Does this make sense? Should a dog be `-99999` years old? No, they should not. They could also set the name to `null`, or the breed to `null`. This is why you would use `private`, as it prevents the user from having access to the variable. The issue is this goes both ways. The user can nota access a `private` variable at all, not even view it. This might be desirable, maybe it is some internal variable that only the object needs to use, and no outside user should ever need. `age` is something the user might need to access. This introduces the idea of getter and setter methods.

Getter and setter methods are public methods that allow the user to get and set the variable in question. These are useful because you, as a programmer, can have some control over what the user is allowed to do with these methods. Lets do a setter first. We would expect it to initially look like
```java
public void setAge(int age){
    this.age = age;
}
```
This is a good start, but you will notice it is effectively equivalent to the `public` variable. They can still pass the integer `-9999` and it would work. Let’s fix this! We can modify our code like this:
```java
public void setAge(int age){
    if(age > 0){
        this.age = age;
    } else {
        this.age = 0;
    }
}
```
Now, if our devious user tries to set the age to some negative number, we can catch them!

A getter is just a public method that returns the value of the instance variable. It would look something like this for age:
```java
public int getAge(){
    return this.age;
}
```
Getters are typically simple, just being a one-line return statement. Some are more sophisticated, and preform some processing on the variable. Importantly, your getter should always return a COPY of the instance variable if you want to protect it. What does this mean? This is a huge rabit hole that has an entire unit deticated to in in CPEN 221/223, but what you need to know now is if it is a primitive type (integers, etc) then returning it directly is fine as Java will return a copy, but if it is a class (String, for example) then see if the class you want to return has a `copy` method, and use it to return a copy of it. Getters are necessary when you want your user to have access to private instance variables!

It is very important that your getter and sett are public methods, as they are otherwise useless!

Now, for the purposes of CPEN 221, ALL INSTANCE VARIABLES SHOULD BE PRIVATE. In real life, it depends on the context. If this is a code base only you are working on, then keep them public if you would like. One benefit of private instance variables is the setters can be useful for catching bugs, as you know something has gone wrong if your code attempts to set an instance variable to something that does not make sense.

For the purposes of this course, and getting you ready for CPEN 221, keep them private.

## What about Methods?

Methods are a bit different. A method the user has not right to use should be private. A great example of this is helper methods. Just like the helper functions you made in APSC 160, helper methods are small methods that are used by other methods to do a very specific action, and generally help make larger methods more readable. For example, say you make a `SoundComparer` class that has a method that compares two soundwaves using least squares. As the name implies, this algorithm has to square numbers at some point, so for readability purposes it might be a good idea to have a private method that squares the input. This squaring method is completely useless for our user, so it makes sense to keep it private.

In summary, if it is a method who’s only purpose is to help another method, keep it private.
