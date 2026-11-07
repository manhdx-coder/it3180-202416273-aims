# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.0.1] - 2026-11-07

### Fixed
- Document case-insensitive title search (#17).

### Added
- Add search_by_category() to search DVDs by category.
- Add sort_by_title() to sort DVDs alphabetically by title.
- Add sort_by_cost() to sort DVDs by ascending cost.

## [1.0.0] - 2026-11-07

### Added
- Add Cart.print_cart() to display cart contents.
- Handle empty cart when printing.
- Add search_by_title() to search DVDs by title.
- Add Vietnamese success message when adding a DVD to cart.

### Fixed
- Fix cart limit validation to reject the 21st DVD (#6).
- Fix cart display and search-related functionality.