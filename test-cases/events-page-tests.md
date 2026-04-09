# GreenCity Events Page Test Cases

---

## 🧪 Test Case 1: Verify events list is displayed

### Title
Events list should be visible on page load

### Preconditions
- User opens the events page
- Internet connection is available

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open browser | - | Browser opened |
| 2 | Navigate to events page | https://www.greencity.cx.ua/#/greenCity/events | Page loads successfully |
| 3 | Observe events section | - | List of events is displayed |
| 4 | Verify number of events | ≥1 | At least 1 event is shown |

---

## 🧪 Test Case 2: Verify event card UI

### Title
Event card displays correct UI elements

### Preconditions
- Events page is open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Select an event card | My super cool event | Card is visible |
| 2 | Verify title | - | Title displayed without truncation |
| 3 | Verify date | 26 Sep 2025 | Date format DD.MM.YYYY |
| 4 | Verify "More" button | - | Button is active |

---

## 🧪 Test Case 3: Verify filter by date

### Title
User can filter events by date

### Preconditions
- Events page is open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open date filter | - | Date filter visible |
| 2 | Select date | 01.04.2026 | Filter applied |
| 3 | Confirm filter | Click Apply | List updates |
| 4 | Verify results | Date ≥ 01.04.2026 | All events match selected date |

---

## 🧪 Test Case 4: Verify filter by category

### Title
User can filter events by category

### Preconditions
- Events page is open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open category filter | - | Category filter visible |
| 2 | Select category | Cleaning | Filter applied |
| 3 | Verify events | - | All events belong to selected category |

---

## 🧪 Test Case 5: Verify invalid filter shows no events

### Title
No events displayed for invalid filter

### Preconditions
- Events page is open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Select date | 01.01.2035 | Filter applied |
| 2 | Observe events | - | List is empty |
| 3 | Verify message | - | "No events found" displayed |

---

## 🧪 Test Case 6: Verify authorized user can open event creation form

### Title
Authorized user can access "Create Event" form

### Preconditions
- User is logged in (Email: testuser@gmail.com)
- Events page is open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click "Create Event" | - | Form opens |
| 2 | Verify URL | /create-event | URL changes |
| 3 | Verify UI | - | Form displayed correctly |

---

## 🧪 Test Case 7: Verify unauthorized user is redirected

### Title
Unauthorized user cannot create event

### Preconditions
- User is NOT logged in
- Events page is open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click "Create Event" | - | Redirect to login page |
| 2 | Verify page | /login | Login page displayed |

---

## 🧪 Test Case 8: Verify event creation with valid data

### Title
User can create an event successfully

### Preconditions
- User is logged in
- Events page is open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Enter title | Tree Planting Kyiv | Accepted |
| 2 | Enter date | 15.04.2026 | Accepted |
| 3 | Enter location | Kyiv, Ukraine | Accepted |
| 4 | Enter description | Planting trees in park | Accepted |
| 5 | Click Submit | - | Event is created and appears in list |

---

## 🧪 Test Case 9: Verify validation errors for empty fields

### Title
Form shows validation errors when fields are empty

### Preconditions
- Event creation form is open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Clear all fields | - | Fields are empty |
| 2 | Click Submit | - | Validation errors displayed |
| 3 | Verify Title field | Empty | "Title is required" |
| 4 | Verify Date field | Empty | "Date is required" |

---

## 🧪 Test Case 10: Verify navigation to event details page

### Title
User can navigate to event details

### Preconditions
- Events list is displayed

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click event | Eco Cleaning Day | Navigation occurs |
| 2 | Verify URL | /events/{id} | URL changes correctly |
| 3 | Verify data | - | Event data matches |

---

## 🧪 Test Case 11: Verify long event title UI

### Title
Long event titles are displayed correctly without breaking UI

### Preconditions
- Event with long title exists

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open Events page | https://www.greencity.cx.ua/#/greenCity/events | Page loaded |
| 2 | Find event | kkkhhhhhhhhhhhhhhhh | Card found |
| 3 | Verify display | - | Text does not overflow |
| 4 | Verify UI | - | Ellipsis "..." or line break appears |

---

## 🧪 Test Case 12: Verify event card clickability

### Title
Event card should be clickable

### Preconditions
- Events list exists

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click on card | Click | Navigation occurs |
| 2 | Verify behavior | - | Event page opens |

---

## 🧪 Test Case 13: Verify cross-browser compatibility

### Title
Events page works correctly in Chrome and Firefox

### Preconditions
- Chrome and Firefox installed

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open in Chrome | Version 122 | Works correctly |
| 2 | Open in Firefox | Version 123 | Works similarly |
| 3 | Compare UI | - | No differences |

---

## 🧪 Test Case 14: Verify search functionality

### Title
User can search events by keyword

### Preconditions
- Events page open
- Events with keyword "eco" exist

### Test Steps
| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open events page | - | Events list is visible |
| 2 | Click search icon | - | Search input appears |
| 3 | Enter keyword | "eco" | Keyword is entered |
| 4 | Submit search | Press Enter | Events list updates |
| 5 | Verify results | - | All events contain keyword "eco" 

---

## 🧪 Test Case 15: Verify user registration for event

### Title
User can register for an event

### Preconditions
- User is logged in
- Event is available

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open event | Some Event | Event page displayed |
| 2 | Click "Join event" | Click | Button active |
| 3 | Confirm | Click Confirm | Registration completed |
| 4 | Verify status | - | "You are registered" displayed |

---

## 🧪 Test Case 16: Verify user cannot register twice

### Title
User cannot register for the same event twice

### Preconditions
- User already registered

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Open event | Some Event | Page open |
| 2 | Click Register | Click | System checks |
| 3 | Verify result | - | Message "Already registered" |

---

## 🧪 Test Case 17: Verify sorting by date

### Title
Events should be sorted by date

### Preconditions
- Multiple events exist

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Select sorting | By date | Applied |
| 2 | Verify order | - | Events sorted by date |

---

## 🧪 Test Case 18: Verify language switch

### Title
User can switch language

### Preconditions
- Events page open

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Locate language switcher | UA/EN | Visible |
| 2 | Select language | English | Language changes |
| 3 | Verify UI | - | All texts in English |

---

## 🧪 Test Case 19: Verify all UI elements translated

### Title
All UI elements should be in selected language

### Preconditions
- English selected

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Verify buttons | - | In English |
| 2 | Verify navigation menu | - | In English |
| 3 | Verify validation messages | - | In English |

---

## 🧪 Test Case 20: Verify no untranslated text

### Title
No untranslated text should be present

### Preconditions
- English selected

### Test Steps

| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Review page | - | No Ukrainian text |
| 2 | Verify form | - | All translated |

---

## 🧪 Test Case 21: Verify date format matches language

### Title
Date format updates according to language

### Preconditions
- Language changed

### Test Steps
| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Select English | - | Language applied |
| 2 | Verify date | 04/15/2026 | Date format changes to MM/DD/YYYY |


---

## 🧪 Test Case 22: Verify invalid email not accepted

### Title
Invalid email format is rejected

### Preconditions
- Registration form available

### Test Steps
| Step | Action | Data | Expected Result |
|------|--------|------|----------------|
| 1 | Click Sign In | - | Login modal appears |
| 2 | Locate email input | - | Email input is visible |
| 3 | Verify initial error | - | No error message displayed |
| 4 | Enter invalid email | "test@@gmail" | Email is entered |
| 5 | Trigger validation | Press Tab | Error message appears |
| 6 | Verify error message | - | "Check that your email address is correct" displayed |