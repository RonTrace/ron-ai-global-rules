# 🤖 AI Global Rules

## Table of Contents
1. [📋 Behavior Guidelines](#behavior-guidelines)
2. [🔌 Plugins](#plugins)
3. [📝 Code Style](#code-style)
4. [🔧 Commands](#shortcodes-and-commands)
5. [🎨 UI Standards](#ui-standards)

## Behavior Guidelines

## Always Do This

- Write clean, maintainable, scalable, and efficient code.
- Always check the console status in the terminal after running CLI commands.
- Always run the app on the same port. Kill the previous version if necessary.

## Break Down Tasks

- Decompose complex requests into manageable steps.
- Present a clear plan before implementing each part.

## Output Focused Communication

- Provide direct, actionable code with minimal explanation.
- Only elaborate when explicitly asked.
## 🔌 Plugins

### Lifeline

- **Description**: Custom plugin for code organization, documentation, and context management
- **Repository**: https://github.com/RonTrace/lifeline
- **IDE Support**: VSCode, Windsurf, Cursor
- **Usage**: This plugin's specific commands are defined in the `shortcodes.md` file
- **Notes**: 
  - All lifeline commands follow a standardized format
  - Refer to the shortcodes file for complete usage instructions
  - This plugin enhances AI coding assistance by providing structured context

### SQLTools

- **Description**: Database management and SQL query execution
- **Repository**: https://marketplace.visualstudio.com/items?itemName=mtxr.sqltools
- **IDE Support**: VSCode, Windsurf, Cursor
- **REQUIRED USAGE**: ALWAYS use SQLTools for database operations; NEVER build connections from scratch
- **Primary Commands**:
  - `sqltools connect` - Connect to the database
  - `sqltools.executeQuery` - Run the current SQL query
  - `sqltools.executeQueryFromFile` - Execute saved queries
- **Supported Databases**:
  - PostgreSQL
  - MySQL
  - SQLite
  - Microsoft SQL Server
  - Oracle
- **Usage Guidelines**:
  - Always verify database connection before running queries
  - Use proper query formatting for readability
  - Apply query limiting (LIMIT/TOP) for large datasets
  - Structure complex queries with CTEs for maintainability
  - NEVER attempt to create custom database connections or use raw database libraries

## 📝 Code Style

- Use 2 spaces for indentation.
- Prefer functional components over class components in React.
- Always include PropTypes for component props.

## 🔧 Commands

## build

When the user types **build**, follow these instructions:

- Follow the directions as described in the **README.md** file in the "Building and Installing Locally" section.

## lifeline

When the user types **lifeline**, follow these instructions:

1. **Create a lifeline markdown file:**

   - Look for a folder in the project called `_lifeline`.
   - If that folder does not exist, create it.
   - Inside that folder, create a file called `_lifeline-[date].md`, where [date] is the current date and time in the format `YYYY-MM-DD-HH-MM-SS`.

2. **Gather context to write inside the lifeline file:**

   - You are writing a prompt for an AI coder.
   - Your prompt should be in XML format with the following structure:
     a. goal
     b. return format
     c. warnings
     d. code map
     e. context
   - In the goal section: Summarize the current project and describe the specific task or problem we are trying to solve.
   - In the return format section: Describe the expected output format of the AI coder's response.
   - In the warnings section: Document any potential issues or warnings that may arise during the AI coder's work. Include issues we have identified.
   - In the code map section: Include a code map of how all the elements we are working with fit together.
   - In the context section: Include any relevant code snippets, comments, or other information that can help the AI coder understand the project context.
   - If applicable, log the intended before and after states of any planned code changes in code blocks (without applying changes to the actual codebase).

3. **Important**

   - Only create the lifeline file.
   - Do not make any modifications to the existing codebase.
   - Do not edit or modify files—just document information inside the lifeline file.
   - Stop working after you've created the lifeline file.

## lifeline read

When the user types **lifeline read**, follow these instructions:

- Find the most recent file in the `_lifeline` folder that starts with `_lifeline-response` and follow the directions outlined in that file step by step.
\n## 🔌 Plugins\n
# Plugins

## Lifeline

## 🎨 UI Standards

## Table of Contents
1. [Layout](#layout)
2. [Sections and Elements](#sections-and-elements)
3. [Naming Conventions](#naming-conventions)
4. [Functionality](#functionality)
5. [Typography](#typography)
6. [Spacing](#spacing)
7. [UI Component Selection](#ui-component-selection)
8. [Specific Patterns and Element Placement](#specific-patterns-and-element-placement)

## Layout

- Use a hierarchical structure for page layouts
- Implement responsive designs for various screen sizes
- Consider the F-pattern and Z-pattern for content placement
- Place key content "above the fold" where possible

### Decision-making process:
1. Identify the primary user goals for the page
2. Sketch a rough layout considering content hierarchy
3. Determine breakpoints for responsive design
4. Iterate and refine based on user testing and feedback

### Example:
```html
<main class="layout">
  <header class="layout__header">...</header>
  <nav class="layout__nav">...</nav>
  <section class="layout__content">
    <article class="layout__main">...</article>
    <aside class="layout__sidebar">...</aside>
  </section>
  <footer class="layout__footer">...</footer>
</main>
```

## Sections and Elements

- Group related content into distinct sections
- Use semantic HTML elements (e.g., `<header>`, `<nav>`, `<main>`, `<footer>`)
- Implement a clear visual hierarchy within sections


### Decision-making process:

1. Analyze the content and identify logical groupings:

1. Group content by topic or function (e.g., product details, user reviews, related items)
2. Separate primary and secondary information
3. Identify content that should be immediately visible vs. content that can be hidden or collapsed



2. Choose appropriate semantic HTML elements
3. Consider the visual weight and importance of each section
4. Ensure accessibility with proper heading structure


### Example:

```html
<section class="product-showcase">
  <h2 class="product-showcase__title">Featured Products</h2>
  <ul class="product-showcase__list">
    <li class="product-showcase__item">
      <article class="product-card">
        <img class="product-card__image" src="product1.jpg" alt="Product 1">
        <h3 class="product-card__title">Product 1</h3>
        <p class="product-card__description">Brief description of Product 1</p>
        <button class="product-card__cta">Add to Cart</button>
      </article>
    </li>
    <li class="product-showcase__item">
      <!-- Similar structure for other products -->
    </li>
  </ul>
</section>
```

## Naming Conventions

- Use BEM (Block Element Modifier) methodology for CSS classes
- Use kebab-case for CSS classes and IDs
- Use PascalCase for React component names
- Use camelCase for JavaScript variables and functions


### Decision-making process:

1. Identify the main component (Block in BEM)
2. Name child elements with double underscores
3. Use modifiers with double dashes for variations
4. Ensure names are descriptive and consistent


### Example:

```javascriptreact
function ProductCard({ product, isFeatured }) {
  return (
    <div className={`product-card ${isFeatured ? 'product-card--featured' : ''}`}>
      <img className="product-card__image" src={product.image || "/placeholder.svg"} alt={product.name} />
      <h3 className="product-card__title">{product.name}</h3>
      <p className="product-card__price">{product.price}</p>
      <button className="product-card__add-to-cart">Add to Cart</button>
    </div>
  );
}
```

## Functionality

- Implement intuitive and expected behaviors
- Provide clear feedback for user actions


### Decision-making process:

1. Define the primary function of each component
2. Consider edge cases and error states
3. Implement appropriate feedback mechanisms


### Examples of intuitive behaviors:

- Buttons change appearance on hover to indicate they're clickable
- Dropdown menus expand on click or hover
- Form fields highlight when focused
- Swiping left/right on mobile for image carousels


### Examples of clear feedback:

- Show a loading spinner when submitting a form
- Display a success message after completing an action
- Highlight selected items in a list
- Show error messages next to form fields with invalid input


### Example:

```javascriptreact
function SubmitButton({ isLoading, onClick }) {
  return (
    <button 
      className={`submit-button ${isLoading ? 'submit-button--loading' : ''}`}
      onClick={onClick}
      disabled={isLoading}
    >
      {isLoading ? (
        <>
          <span className="submit-button__spinner"></span>
          Submitting...
        </>
      ) : 'Submit'}
    </button>
  );
}

function FormField({ label, value, onChange, error }) {
  return (
    <div className={`form-field ${error ? 'form-field--error' : ''}`}>
      <label className="form-field__label">{label}</label>
      <input 
        className="form-field__input"
        value={value}
        onChange={onChange}
      />
      {error && <p className="form-field__error">{error}</p>}
    </div>
  );
}
```

## Typography

- Establish a clear typographic hierarchy
- Use a limited set of font sizes and weights
- Ensure sufficient contrast for readability
- Implement appropriate line heights and letter spacing


### Decision-making process:

1. Choose a primary font family (and secondary if needed)
2. Define a typographic scale (e.g., 1.2 or 1.5 ratio)
3. Assign specific sizes to different text elements (h1, h2, p, etc.)
4. Test readability on various devices and adjust as needed


### Guidelines for appropriate typography:

- Line height: 1.5 for body text, 1.2 for headings
- Letter spacing: -0.02em for headings, normal for body text
- Adjust based on font choice and size (larger text often needs tighter line height)


### Example:

```css
:root {
  --font-primary: 'Roboto', sans-serif;
  --font-size-base: 16px;
  --line-height-base: 1.5;
  --line-height-heading: 1.2;
}

body {
  font-family: var(--font-primary);
  font-size: var(--font-size-base);
  line-height: var(--line-height-base);
}

h1, h2, h3, h4, h5, h6 {
  line-height: var(--line-height-heading);
  letter-spacing: -0.02em;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

h2 {
  font-size: 2rem;
  margin-bottom: 0.8rem;
}

p {
  margin-bottom: 1rem;
}
```

## Spacing

- Use a consistent spacing system
- Implement appropriate white space for readability
- Ensure sufficient spacing between interactive elements
- Adjust spacing for different screen sizes


### Decision-making process:

1. Define a base spacing unit (e.g., 8px)
2. Create a spacing scale (e.g., 8px, 16px, 24px, 32px, 48px)
3. Apply spacing consistently to margins and paddings
4. Adjust spacing at different breakpoints for responsiveness


### Example:

```css
:root {
  --spacing-unit: 8px;
  --spacing-xs: calc(var(--spacing-unit) * 0.5);
  --spacing-sm: calc(var(--spacing-unit) * 1);
  --spacing-md: calc(var(--spacing-unit) * 2);
  --spacing-lg: calc(var(--spacing-unit) * 3);
  --spacing-xl: calc(var(--spacing-unit) * 4);
}

.card {
  padding: var(--spacing-md);
  margin-bottom: var(--spacing-lg);
}

.card__title {
  margin-bottom: var(--spacing-sm);
}

.card__content {
  margin-bottom: var(--spacing-md);
}

@media (min-width: 768px) {
  .card {
    padding: var(--spacing-lg);
  }
}
```

## UI Component Selection

- Choose components based on the nature of the data or action
- Consider the amount of available screen space
- Think about the frequency of use and user goals
- Maintain consistency across the application


### Decision-making process:

1. Identify the type of data or action required
2. Consider the context and available space
3. Evaluate user familiarity and expectations
4. Choose the most appropriate component from the guidelines
5. Ensure the chosen component is accessible and responsive


### Examples of frequency of use and user goals:

- Frequently used actions (e.g., add to cart) should be prominently placed and easily accessible
- Less common actions (e.g., account settings) can be in dropdown menus or secondary navigation
- Primary user goals (e.g., finding a product) should be supported by prominent search bars or category navigation


### Examples of maintaining consistency:

- Use the same color scheme throughout the app
- Maintain consistent button styles for primary and secondary actions
- Use the same icon set across all pages
- Keep navigation in the same location across different pages


### Examples:

For selection from a small set of options:

```javascriptreact
function ColorPicker({ colors, selectedColor, onSelect }) {
  return (
    <div className="color-picker">
      {colors.map(color => (
        <button
          key={color}
          className={`color-picker__option ${selectedColor === color ? 'color-picker__option--selected' : ''}`}
          style={{ backgroundColor: color }}
          onClick={() => onSelect(color)}
          aria-label={`Select ${color}`}
        />
      ))}
    </div>
  );
}
```

For a range of values:

```javascriptreact
function PriceRangeSlider({ min, max, value, onChange }) {
  return (
    <div className="price-range">
      <label htmlFor="price-slider" className="price-range__label">Price Range:</label>
      <input
        id="price-slider"
        type="range"
        min={min}
        max={max}
        value={value}
        onChange={onChange}
        className="price-range__slider"
      />
      <output className="price-range__value">${value}</output>
    </div>
  );
}
```

## Specific Patterns and Element Placement

### 1. Row vs. Column Layout:

- Use rows for related items of equal importance (e.g., product cards in a catalog)
- Use columns for hierarchical information (e.g., sidebar navigation next to main content)
- Switch from row to column layout on smaller screens for better readability


Example:

```html
<div class="product-grid">
  <div class="product-grid__item">Product 1</div>
  <div class="product-grid__item">Product 2</div>
  <div class="product-grid__item">Product 3</div>
</div>

<div class="page-layout">
  <nav class="page-layout__sidebar">Sidebar Navigation</nav>
  <main class="page-layout__main">Main Content</main>
</div>
```

### 2. Button Placement:

- Primary action buttons (e.g., "Submit", "Save") should be on the right or bottom of forms
- Secondary action buttons (e.g., "Cancel", "Back") should be to the left of or above primary buttons
- In lists or tables, place edit/delete buttons to the right of each item
- For mobile, important buttons should be within thumb reach (bottom of the screen)


Example:

```html
<form class="user-form">
  <!-- Form fields here -->
  <div class="user-form__actions">
    <button type="button" class="button button--secondary">Cancel</button>
    <button type="submit" class="button button--primary">Save</button>
  </div>
</form>

<ul class="item-list">
  <li class="item-list__item">
    Item 1
    <div class="item-list__actions">
      <button class="button button--edit">Edit</button>
      <button class="button button--delete">Delete</button>
    </div>
  </li>
  <!-- More list items -->
</ul>
```

### 3. Form Layout:

- Labels should be above input fields for better readability
- Group related fields together (e.g., first name and last name)
- Place optional fields at the bottom of the form
- Align labels and fields in a single column for mobile views


Example:

```html
<form class="contact-form">
  <div class="form-group">
    <label for="name" class="form-label">Name</label>
    <input type="text" id="name" class="form-input" required>
  </div>
  <div class="form-group">
    <label for="email" class="form-label">Email</label>
    <input type="email" id="email" class="form-input" required>
  </div>
  <div class="form-group">
    <label for="message" class="form-label">Message</label>
    <textarea id="message" class="form-input" required></textarea>
  </div>
  <div class="form-group">
    <label for="phone" class="form-label">Phone (optional)</label>
    <input type="tel" id="phone" class="form-input">
  </div>
  <button type="submit" class="button button--primary">Send</button>
</form>
```

### 4. Navigation Placement:

- Primary navigation: Horizontal bar at the top for desktop, hamburger menu for mobile
- Secondary navigation: Left sidebar for desktop, collapsible menu for mobile
- Footer navigation: Less important links, legal information, social media links


Example:

```html
<header class="site-header">
  <nav class="primary-nav">
    <ul class="primary-nav__list">
      <li class="primary-nav__item"><a href="#home">Home</a></li>
      <li class="primary-nav__item"><a href="#products">Products</a></li>
      <li class="primary-nav__item"><a href="#about">About</a></li>
      <li class="primary-nav__item"><a href="#contact">Contact</a></li>
    </ul>
  </nav>
</header>

<div class="page-layout">
  <nav class="secondary-nav">
    <ul class="secondary-nav__list">
      <li class="secondary-nav__item"><a href="#category1">Category 1</a></li>
      <li class="secondary-nav__item"><a href="#category2">Category 2</a></li>
      <li class="secondary-nav__item"><a href="#category3">Category 3</a></li>
    </ul>
  </nav>
  <main class="main-content">
    <!-- Main content here -->
  </main>
</div>

<footer class="site-footer">
  <nav class="footer-nav">
    <ul class="footer-nav__list">
      <li class="footer-nav__item"><a href="#privacy">Privacy Policy</a></li>
      <li class="footer-nav__item"><a href="#terms">Terms of Service</a></li>
      <li class="footer-nav__item"><a href="#sitemap">Sitemap</a></li>
    </ul>
  </nav>
  <div class="social-links">
    <!-- Social media links here -->
  </div>
</footer>
```

### 5. Content Hierarchy:

- Most important information should be at the top left (for left-to-right languages)
- Use size, color, and whitespace to create visual hierarchy
- Implement progressive disclosure: show basic info first, details on demand


Example:

```html
<article class="product-detail">
  <h1 class="product-detail__title">Product Name</h1>
  <p class="product-detail__price">$99.99</p>
  <div class="product-detail__summary">
    <p class="product-detail__description">Brief product description here.</p>
    <button class="product-detail__cta button button--primary">Add to Cart</button>
  </div>
  <details class="product-detail__more-info">
    <summary>More Information</summary>
    <p>Detailed product information goes here...</p>
  </details>
</article>
```

### 6. Call-to-Action (CTA) Placement:

- Primary CTA should be above the fold and visually distinct
- For long pages, repeat the CTA at the bottom
- In product pages, place "Add to Cart" button near the product image and price


Example:

```html
<section class="hero">
  <h1 class="hero__title">Welcome to Our Store</h1>
  <p class="hero__subtitle">Find the best products at great prices</p>
  <a href="#shop" class="hero__cta button button--large">Shop Now</a>
</section>

<section class="product-showcase">
  <!-- Product list here -->
</section>

<section class="cta-bottom">
  <h2 class="cta-bottom__title">Ready to start shopping?</h2>
  <a href="#shop" class="cta-bottom__button button button--large">Shop Now</a>
</section>
```

### 7. Image Placement:

- For product pages: Large image on the left, details on the right
- For articles: Hero image at the top, inline images to break up text
- For profiles: Avatar top left or centered, depending on layout


Example:

```html
<article class="product-page">
  <div class="product-page__image">
    <img src="product-image.jpg" alt="Product Name">
  </div>
  <div class="product-page__details">
    <h1 class="product-page__title">Product Name</h1>
    <p class="product-page__price">$99.99</p>
    <p class="product-page__description">Product description here...</p>
    <button class="product-page__cta button button--primary">Add to Cart</button>
  </div>
</article>

<article class="blog-post">
  <img src="hero-image.jpg" alt="Blog Post Title" class="blog-post__hero">
  <h1 class="blog-post__title">Blog Post Title</h1>
  <p>First paragraph of the blog post...</p>
  <img src="inline-image-1.jpg" alt="Relevant image" class="blog-post__inline-image">
  <p>Second paragraph of the blog post...</p>
</article>

<div class="user-profile">
  <img src="avatar.jpg" alt="User Name" class="user-profile__avatar">
  <h2 class="user-profile__name">User Name</h2>
  <p class="user-profile__bio">User bio goes here...</p>
</div>
```

### 8. Filtering and Sorting:

- Place filter options in a left sidebar for desktop, collapsible top bar for mobile
- Sorting options should be above and right-aligned with the list of items


Example:

```html
<div class="product-listing">
  <aside class="product-listing__filters">
    <!-- Filter options here -->
  </aside>
  <main class="product-listing__content">
    <div class="product-listing__sort">
      <label for="sort-select">Sort by:</label>
      <select id="sort-select" class="sort-select">
        <option value="price-asc">Price: Low to High</option>
        <option value="price-desc">Price: High to Low</option>
        <option value="name-asc">Name: A to Z</option>
        <option value="name-desc">Name: Z to A</option>
      </select>
    </div>
    <div class="product-listing__grid">
      <!-- Product items here -->
    </div>
  </main>
</div>
```

### 9. Pagination vs. Infinite Scroll:

- Use pagination for structured content (e.g., search results, product catalogs)
- Use infinite scroll for social media feeds or homogeneous content streams


Example (Pagination):

```html
<nav class="pagination" aria-label="Page navigation">
  <ul class="pagination__list">
    <li class="pagination__item"><a href="#" class="pagination__link">Previous</a></li>
    <li class="pagination__item"><a href="#" class="pagination__link">1</a></li>
    <li class="pagination__item"><a href="#" class="pagination__link pagination__link--active">2</a></li>
    <li class="pagination__item"><a href="#" class="pagination__link">3</a></li>
    <li class="pagination__item"><a href="#" class="pagination__link">Next</a></li>
  </ul>
</nav>
```

### 10. Modal Dialogs:

- Use for focused tasks that require immediate attention
- Center on the screen with a semi-transparent overlay behind
- Ensure they're dismissible by clicking outside or a clear "close" button


Example:

```javascriptreact
function Modal({ isOpen, onClose, children }) {
  if (!isOpen) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal" onClick={e => e.stopPropagation()}>
        <button className="modal__close" onClick={onClose}>&times;</button>
        <div className="modal__content">
          {children}
        </div>
      </div>
    </div>
  );
}
```

### 11. Tooltip and Help Text:

- Place tooltips above the element they describe, unless space constraints require otherwise
- For form fields, place help text below the input


Example:

```javascriptreact
function FormField({ label, helpText, ...props }) {
  return (
    <div className="form-field">
      <label className="form-field__label">{label}</label>
      <input className="form-field__input" {...props} />
      {helpText && <p className="form-field__help">{helpText}</p>}
    </div>
  );
}

function TooltipButton({ text, tooltip }) {
  return (
    <div className="tooltip-container">
      <button className="button">{text}</button>
      <span className="tooltip">{tooltip}</span>
    </div>
  );
}
```

These guidelines and examples provide a comprehensive framework for making decisions about UI design and element placement. Remember to always consider the specific context of your application and conduct user testing to refine your designs.

