# Advertising your app’s assignable content

Assemble a hierarchy of contexts and declare your app’s assignable content.

## Discussion

A context, stored as a [`CLSContext`](/documentation/ClassKit/CLSContext) instance, represents an area within your app, such as a book chapter or a game level, that teachers can assign to students as tasks. You create a hierarchy of contexts to enable teachers to browse and assign your app’s content. You provide deep links to the content that the contexts represent to help teachers guide students to your content. You then activate and deactivate contexts as users move through your app.

### Identify your app’s assignable tasks

Before you write any new code, decide which parts of your existing app correspond to tasks that a teacher might want to assign to students. For example, a textbook reader app might divide textbooks into chapters and sections, while offering tests and quizzes to measure the reader’s retention of the material. So the app’s assignable tasks fall into a hierarchical structure with the app at the top and tests and quizzes at the bottom.

![Diagram showing a context hierarchy corresponding to a textbook reader.](images/com.apple.classkit/media-2969445@2x.png)

Every app that adopts ClassKit has a single, predefined top-level context called the main app context. To this, you add one or more child contexts representing assignable tasks, each potentially with descendants of its own representing subtasks.

Organize the hierarchy so that it makes sense to teachers creating assignments. For example, the lowest level contexts should represent indivisible units of work, like a quiz. Don’t define a different context for each question of a quiz when you expect teachers to assign the entire quiz as a single task. Instead, use a single context to represent the whole quiz.

Do use contexts to group other contexts in a way that allows teachers to extract useful metrics. A teacher might be interested in a student’s progress not only through a particular section of a textbook, but also through the entire chapter in which that section appears, as well as through the book as a whole. You can design a context hierarchy up to eight levels deep, including the main app context.

### Tell ClassKit about your content

For teachers to be able to assign your app’s content, they have to be able to see it in the Schoolwork app. Schoolwork becomes aware of your content after you tell ClassKit about it. So your next task is to declare the existence of all your contexts to ClassKit. This results in a navigable table of contents in the Schoolwork app that teachers can browse when creating assignments.

You declare a context by requesting it from the data store — the shared [`CLSDataStore`](/documentation/ClassKit/CLSDataStore) instance — using an identifier that you assign. The act of asking for a context tells ClassKit that it exists, and where it lives in the context hierarchy. For details, see <doc://com.apple.classkit/documentation/ClassKit/declaring-your-app-s-context-hierarchy>.

### Create new contexts when needed

When you ask the data store for a context, whether to declare its existence or to activate and use it, the data store looks to see if that context already exists in its database. If so, the data store returns the stored context. If not, the data store asks its delegate to build the context. You adopt the [`CLSDataStoreDelegate`](/documentation/ClassKit/CLSDataStoreDelegate) protocol to build contexts when they don’t already exist, as described in <doc://com.apple.classkit/documentation/ClassKit/building-missing-contexts>.

### Help teachers guide students to your content

Tapping in the Schoolwork app on an assignment associated with your ClassKit enabled app generates a deep link to your app. The link arrives in the form of either a user activity or a universal link, depending on how you’ve configured the context corresponding to the assignment. By properly handling this link, as described in <doc://com.apple.classkit/documentation/ClassKit/linking-directly-to-assignments>, you help teachers to guide students to the content that’s important to them.

### Activate contexts when users begin a task

When the user begins a task that corresponds to one of your app’s contexts, you activate the context. Later, when the user completes the task, you deactivate the context. See <doc://com.apple.classkit/documentation/ClassKit/informing-classkit-that-a-task-is-about-to-begin> for details.

### Ignore the user’s role

Certain aspects of context management only pertain to particular users. For example, students never see a complete table of contents of your app’s content in Schoolwork, so they don’t need to declare or build all contexts. They really only need to build the contexts associated with specific assignments that they receive. However, for privacy reasons, ClassKit doesn’t tell you the current user’s role. So your app must perform all operations for all users and let ClassKit figure out what data it actually needs. For more details, see <doc://com.apple.classkit/documentation/ClassKit/about-classkit-and-user-roles>.

## Topics

### Context management

  <doc://com.apple.classkit/documentation/ClassKit/declaring-your-app-s-context-hierarchy>

  <doc://com.apple.classkit/documentation/ClassKit/building-missing-contexts>

  <doc://com.apple.classkit/documentation/ClassKit/informing-classkit-that-a-task-is-about-to-begin>

### Deep links

  <doc://com.apple.classkit/documentation/ClassKit/linking-directly-to-assignments>

### Bookmarks

  <doc://com.apple.classkit/documentation/ClassKit/creating-bookmarks-and-assignments-from-your-app>



---

Copyright &copy; 2026 Apple Inc. All rights reserved. | [Terms of Use](https://www.apple.com/legal/internet-services/terms/site.html) | [Privacy Policy](https://www.apple.com/privacy/privacy-policy)
