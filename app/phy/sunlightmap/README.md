




npm install -g @ionic/cli
npm install -g @ionic/cli native-run cordova-res


ionic start sunlightmap tabs
ionic start sunlightmap tabs --type angular  --capacitor

Your Ionic app is ready! Follow these next steps:

- Go to your new project: cd ./sunlightmap
- Run ionic serve within the app directory to see your app in the browser
- Run ionic capacitor add to add a native iOS or Android project using Capacitor
- Generate your app icon and splash screens using cordova-res --skip-config --copy
- Explore the Ionic docs for components, tutorials, and more: https://ion.link/docs
- Building an enterprise app? Ionic has Enterprise Support and Features: https://ion.link/enterprise-edition

? Would you like to build your app with NgModules or Standalone Components?
 Standalone components are a new way to build with Angular that simplifies the way you build your app.
 To learn more, visit the Angular docs:
 https://angular.io/guide/standalone-components

 (Use arrow keys)
❯ NgModules
  Standalone

  
> ionic integrations enable capacitor --quiet -- sunlightmap io.ionic.starter
> npm i --save -E @capacitor/core@latest

shopt -s dotglob
mv sunlightmap/* .

ionic capacitor add android
> npm.cmd i -E @capacitor/android@5.2.3

ionic serve --livereload --consolelogs --no-open

ionic g page map
ionic g page settings
ionic g page about

ionic g service services/settings


ionic build 
#ionic build --prod
#ionic build --watch

ionic cap copy



http for map

npm install @angular/common/http








Certainly! Angular is a structured and modular framework, and understanding its primary building blocks like Modules, Pages, and Components is crucial. Let's break down these concepts:

### 1. **Modules (`NgModule`)**

In Angular, a module is a mechanism to group together related components, directives, pipes, and services that are bound to a common domain, workflow, or related set of capabilities. Essentially, it's a way to organize an application and manage dependencies.

- **Root Module**: Every Angular app has at least one module, known as the root module, conventionally named `AppModule`.
  
- **Feature Modules**: Apart from the root module, larger apps may have feature modules to encapsulate specific application features.

- **Lazy Loading**: Feature modules can be lazy-loaded, meaning Angular will only load them when they are needed, enhancing app performance.

- **Decorators**: The module is typically decorated with `@NgModule`, which takes metadata to specify how to compile a component's template and how to create an injector at runtime.

- **Imports and Exports**: Modules can import functionality from other modules and export their own functionality for use by other modules.

### 2. **Components**

At the core of Angular are components. They control a portion of the user interface or a view.

- **Templates**: Each component has an associated template that defines how its view is rendered.

- **Lifecycle**: Components have a lifecycle, and you can hook into specific events like initialization (`ngOnInit`) and cleanup (`ngOnDestroy`).

- **Decorator**: Components use the `@Component` decorator which provides metadata like selector (to use in templates), template URL, styles URL, etc.

- **Tree Structure**: Components have a tree structure, with one root component and many nested child components.

### 3. **Pages**

While "Pages" is not an Angular-specific concept, in the context of frameworks like Ionic (which combines Angular with mobile-focused components), "Pages" refer to the main views or screens in your app.

- **A Page is a Component**: In Angular terms, a page is just another component. But by convention or pattern, it represents a full view or screen.

- **Routing**: In apps that use a router (like Ionic apps or SPA web apps), each page is associated with a route. When that route is activated, the page's component is loaded.

- **Structure**: Like any component, pages have their own template, styles, and logic. But they often also include various child components that make up the pieces of that view.

---

In summary, you can think of an Angular application as a tree of components (including pages), organized into modules for better structuring and lazy loading. The app starts with the root module, which bootstraps the root component, and from there, child components (or pages) take over, each controlling their own part of the screen or view.












In an Ionic (combined with Angular) application, a clear structure is essential for maintainability, scalability, and understandability of the codebase. The following is a recommended structure for components and services:

### 1. **App Structure Overview**:

An Ionic project initialized with the CLI has the following basic structure:

```
- src/
  - app/
    - home/ (example of a page)
    - app-routing.module.ts
    - app.component.html
    - app.component.ts
    - app.module.ts
  - assets/
  - environments/
  - index.html
  - ...
```

### 2. **Components**:

Components are the building blocks of the UI. They can be small UI parts (like a custom button) or entire pages. Here's how you might organize them:

- **Pages**: Each page in an Ionic app is essentially a component, but we often treat pages as special entities since they correspond to whole screens or routes. They reside directly inside the `app` directory.

  ```
  - app/
    - home/
      - home.page.html
      - home.page.scss
      - home.page.ts
      - home.module.ts
    - profile/
    - settings/
  ```

- **Shared Components**: Components that are reused across multiple pages or other components can be placed in a shared or components directory.

  ```
  - app/
    - components/
      - custom-button/
        - custom-button.component.html
        - custom-button.component.ts
        - custom-button.component.scss
      - custom-card/
  ```

  Register shared components in a shared module and import this module wherever the components are needed. 

  ```typescript
  // shared/components.module.ts
  import { NgModule } from '@angular/core';
  import { CustomButtonComponent } from './custom-button/custom-button.component';

  @NgModule({
    declarations: [CustomButtonComponent],
    exports: [CustomButtonComponent],
  })
  export class ComponentsModule { }
  ```

### 3. **Services**:

Services typically contain shared functionality that might be used by many components or other services.

- **Organization**: Create a separate directory for services:

  ```
  - app/
    - services/
      - user.service.ts
      - api.service.ts
  ```

- **Service Module**: For larger applications, you can have a dedicated module for services (though it's not as common as having a shared module for components). This module would then be imported into the root or feature modules where the services are required.

### 4. **Utility and Helpers**:

You might also have utility functions, classes, or constants. These can be organized in a `utils` or `helpers` directory.

```
- app/
  - helpers/
    - utilities.ts
    - constants.ts
```

### 5. **Barrel Files** (optional):

For ease of import, especially in directories with numerous services or components, you can use a barrel file (typically named `index.ts`). This allows multiple exports from a single module, simplifying imports.

### 6. **Further Organization**:

For very large applications, consider feature modules, organizing services and components by domain or functionality. Lazy-loading can then be applied to these feature modules to optimize app performance.

---

This structure is a recommendation and may vary based on the complexity and requirements of your project. The main goal is to maintain a clean, modular, and understandable directory structure.




















## Specs




### 1. Program Description and Features:

**Program Name**: Sunlight Map`  
**Purpose**: Show a day and night map of the planet at the current time
**Target Users**: End users

**Technology**:

1. this is an Android app.
2. to be written with Ionic in version 6 or version 7.


**Features**: 

1. **User Login**:  
   - No user login.
   - also no user data stored anywhere.

2. **Data Management**:  
   - Users should be able to create, read, update, and delete (CRUD) their data.
   - Data should be stored within the app.
   - the data is a set of settings, and a list of geolocations

3. **Home Page**:  
   - When opening the app, The user should see a page with a map
   - the map is an image
   - the base image is requested from an API endpoint and comes as base64 data
   - on top of this base map the user's ist of geolocations is shown

4. **Notifications**:  
   - no notifications

5. **API Integration**:
   - The only consumes 1 endpoint

6. **Accessibility**:
   - Default Android app accessibility








### **Sunlight Map App UI Specification (Android)**


#### **1. Design System & Style Guide**:

- **Colors**:
  - Primary: `#859900`
  - Secondary: `#fdfde3`
  - Accent: `#cb4b16`

- **Typography**:
  - **Main Font**: Roboto (default for Android)
    - **Header**: Roboto Medium, 20sp
    - **Sub-header**: Roboto Regular, 18sp
    - **Body Text**: Roboto Light, 16sp
    - **Button Text**: Roboto Medium, 18sp

- **Iconography**: Use Material Design Icons, ensuring they are of a size comfortable for touch (at least 48dp x 48dp touch targets).



#### **2. Screen Layouts**:

##### **a. Home Page**:

- **Layout**: Full-screen map view.

  - **Map View**:
    - **Type**: Full screen, edge to edge.
    - **Interaction**: Pinch to zoom, drag to pan. Tap on geolocation markers to view details.
    - cache the map for 10 minutes
  
  - **Floating Action Button (FAB)**: Positioned at the bottom right.
    - **Icon**: `add_location` (Material Design icon for adding location).
    - **Action**: Tapping opens a modal or bottom sheet to input a new geolocation.
  
  - **Location Form**: Positioned at the bottom right.
    - **Location**:
    - **Button**:
    - … (error handling)
  
  - **Bottom Bar**:
    - **Background**: Semi-transparent black.
    - **Title**: Centered, "Sunlight Map", Roboto Medium, 20sp, White.
    - **Left Action**: Cog menu icon to open a settings page

- **Transitions**: Use Android's standard Material Design page slide animation for modal or bottom sheet appearances.

#### **3. Feedback & Interactions**:

- **Settings**: The user can select between 3 map centers: AMericas, Greenwich, Pacific

- **Adding geolocation**: a reverse geocoder that takes a city name, requests the geolocation and stores the latitude and longitude. Additionally a title field for the user to enter up to 32 charteacters 

- **opening geolocation markers**: a popup or modal with the title and the location name 

- **fetching map**: show a spinner. if timeout after 10 seconds show popup or similar "offline. please try later" 

- **Toasts**: Use Android's toast messages for feedback, e.g., "Geolocation added!", "Failed to fetch map. Check your connection."

- **Loading Indicator**: A circular progress spinner (Material Design default) centered on the screen when waiting for the map to load.


#### **4. Accessibility**:

- **Touch Targets**: Ensure all tappable elements like the FAB and geolocation markers are at least 48dp x 48dp in size.

- **Colors**: Ensure sufficient contrast between text and its background. For instance, the white text on the semi-transparent black top bar should be readable.

- **VoiceOver**: Ensure every interactive element has a descriptive label for screen readers. For example, the FAB should have a label like "Add new geolocation."













