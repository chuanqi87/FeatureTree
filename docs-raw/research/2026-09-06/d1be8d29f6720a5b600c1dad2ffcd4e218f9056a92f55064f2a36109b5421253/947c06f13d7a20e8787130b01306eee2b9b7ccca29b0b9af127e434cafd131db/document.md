# java.text

Added in [API level 1](https://developer.android.com/guide/topics/manifest/uses-sdk-element#ApiLevels)

# java.text

Provides classes and interfaces for handling text, dates, numbers,
and messages in a manner independent of natural languages. This
means your main application or applet can be written to be
language-independent, and it can rely upon separate,
dynamically-linked localized resources. This allows the flexibility
of adding localizations for new localizations at any time.

These classes are capable of formatting dates, numbers, and
messages, parsing; searching and sorting strings; and iterating
over characters, words, sentences, and line breaks. This package
contains three main groups of classes and interfaces:

* Classes for iteration over text
* Classes for formatting and parsing
* Classes for string collation

## Interfaces

|  |  |
| --- | --- |
| [AttributedCharacterIterator](https://developer.android.com/reference/java/text/AttributedCharacterIterator) | An `AttributedCharacterIterator` allows iteration through both text and related attribute information. |
| [CharacterIterator](https://developer.android.com/reference/java/text/CharacterIterator) | This interface defines a protocol for bidirectional iteration over text. |

## Classes

|  |  |
| --- | --- |
| [Annotation](https://developer.android.com/reference/java/text/Annotation) | An Annotation object is used as a wrapper for a text attribute value if the attribute has annotation characteristics. |
| [AttributedCharacterIterator.Attribute](https://developer.android.com/reference/java/text/AttributedCharacterIterator.Attribute) | Defines attribute keys that are used to identify text attributes. |
| [AttributedString](https://developer.android.com/reference/java/text/AttributedString) | An AttributedString holds text and related attribute information. |
| [Bidi](https://developer.android.com/reference/java/text/Bidi) | This class implements the Unicode Bidirectional Algorithm. |
| [BreakIterator](https://developer.android.com/reference/java/text/BreakIterator) | The `BreakIterator` class implements methods for finding the location of boundaries in text. |
| [ChoiceFormat](https://developer.android.com/reference/java/text/ChoiceFormat) | A `ChoiceFormat` allows you to attach a format to a range of numbers. |
| [CollationElementIterator](https://developer.android.com/reference/java/text/CollationElementIterator) | The `CollationElementIterator` class is used as an iterator to walk through each character of an international string. |
| [CollationKey](https://developer.android.com/reference/java/text/CollationKey) | A `CollationKey` represents a `String` under the rules of a specific `Collator` object. |
| [Collator](https://developer.android.com/reference/java/text/Collator) | The `Collator` class performs locale-sensitive `String` comparison. |
| [DateFormat](https://developer.android.com/reference/java/text/DateFormat) | `DateFormat` is an abstract class for date/time formatting subclasses which formats and parses dates or time in a language-independent manner. |
| [DateFormat.Field](https://developer.android.com/reference/java/text/DateFormat.Field) | Defines constants that are used as attribute keys in the `AttributedCharacterIterator` returned from `DateFormat.formatToCharacterIterator` and as field identifiers in `FieldPosition`. |
| [DateFormatSymbols](https://developer.android.com/reference/java/text/DateFormatSymbols) | `DateFormatSymbols` is a public class for encapsulating localizable date-time formatting data, such as the names of the months, the names of the days of the week, and the time zone data. |
| [DecimalFormat](https://developer.android.com/reference/java/text/DecimalFormat) | `DecimalFormat` is a concrete subclass of `NumberFormat` that formats decimal numbers. |
| [DecimalFormatSymbols](https://developer.android.com/reference/java/text/DecimalFormatSymbols) | This class represents the set of symbols (such as the decimal separator, the grouping separator, and so on) needed by `DecimalFormat` to format numbers. |
| [FieldPosition](https://developer.android.com/reference/java/text/FieldPosition) | `FieldPosition` is a simple class used by `Format` and its subclasses to identify fields in formatted output. |
| [Format](https://developer.android.com/reference/java/text/Format) | `Format` is an abstract base class for formatting locale-sensitive information such as dates, messages, and numbers. |
| [Format.Field](https://developer.android.com/reference/java/text/Format.Field) | Defines constants that are used as attribute keys in the `AttributedCharacterIterator` returned from `Format.formatToCharacterIterator` and as field identifiers in `FieldPosition`. |
| [MessageFormat](https://developer.android.com/reference/java/text/MessageFormat) | `MessageFormat` provides a means to produce concatenated messages in a language-neutral way. |
| [MessageFormat.Field](https://developer.android.com/reference/java/text/MessageFormat.Field) | Defines constants that are used as attribute keys in the `AttributedCharacterIterator` returned from `MessageFormat.formatToCharacterIterator`. |
| [Normalizer](https://developer.android.com/reference/java/text/Normalizer) | This class provides the method `normalize` which transforms Unicode text into an equivalent composed or decomposed form, allowing for easier sorting and searching of text. |
| [NumberFormat](https://developer.android.com/reference/java/text/NumberFormat) | `NumberFormat` is the abstract base class for all number formats. |
| [NumberFormat.Field](https://developer.android.com/reference/java/text/NumberFormat.Field) | Defines constants that are used as attribute keys in the `AttributedCharacterIterator` returned from `NumberFormat.formatToCharacterIterator` and as field identifiers in `FieldPosition`. |
| [ParsePosition](https://developer.android.com/reference/java/text/ParsePosition) | `ParsePosition` is a simple class used by `Format` and its subclasses to keep track of the current position during parsing. |
| [RuleBasedCollator](https://developer.android.com/reference/java/text/RuleBasedCollator) | The `RuleBasedCollator` class is a concrete subclass of `Collator` that provides a simple, data-driven, table collator. |
| [SimpleDateFormat](https://developer.android.com/reference/java/text/SimpleDateFormat) | `SimpleDateFormat` is a concrete class for formatting and parsing dates in a locale-sensitive manner. |
| [StringCharacterIterator](https://developer.android.com/reference/java/text/StringCharacterIterator) | `StringCharacterIterator` implements the `CharacterIterator` protocol for a `String`. |

## Enums

|  |  |
| --- | --- |
| [Normalizer.Form](https://developer.android.com/reference/java/text/Normalizer.Form) | This enum provides constants of the four Unicode normalization forms that are described in [Unicode Standard Annex #15 — Unicode Normalization Forms](https://www.unicode.org/reports/tr15/) and two methods to access them. |

## Exceptions

|  |  |
| --- | --- |
| [ParseException](https://developer.android.com/reference/java/text/ParseException) | Signals that an error has been reached unexpectedly while parsing. |

* ## Interfaces

  + [AttributedCharacterIterator](https://developer.android.com/reference/java/text/AttributedCharacterIterator)
  + [CharacterIterator](https://developer.android.com/reference/java/text/CharacterIterator)
* ## Classes

  + [Annotation](https://developer.android.com/reference/java/text/Annotation)
  + [AttributedCharacterIterator.Attribute](https://developer.android.com/reference/java/text/AttributedCharacterIterator.Attribute)
  + [AttributedString](https://developer.android.com/reference/java/text/AttributedString)
  + [Bidi](https://developer.android.com/reference/java/text/Bidi)
  + [BreakIterator](https://developer.android.com/reference/java/text/BreakIterator)
  + [ChoiceFormat](https://developer.android.com/reference/java/text/ChoiceFormat)
  + [CollationElementIterator](https://developer.android.com/reference/java/text/CollationElementIterator)
  + [CollationKey](https://developer.android.com/reference/java/text/CollationKey)
  + [Collator](https://developer.android.com/reference/java/text/Collator)
  + [DateFormat](https://developer.android.com/reference/java/text/DateFormat)
  + [DateFormat.Field](https://developer.android.com/reference/java/text/DateFormat.Field)
  + [DateFormatSymbols](https://developer.android.com/reference/java/text/DateFormatSymbols)
  + [DecimalFormat](https://developer.android.com/reference/java/text/DecimalFormat)
  + [DecimalFormatSymbols](https://developer.android.com/reference/java/text/DecimalFormatSymbols)
  + [FieldPosition](https://developer.android.com/reference/java/text/FieldPosition)
  + [Format](https://developer.android.com/reference/java/text/Format)
  + [Format.Field](https://developer.android.com/reference/java/text/Format.Field)
  + [MessageFormat](https://developer.android.com/reference/java/text/MessageFormat)
  + [MessageFormat.Field](https://developer.android.com/reference/java/text/MessageFormat.Field)
  + [Normalizer](https://developer.android.com/reference/java/text/Normalizer)
  + [NumberFormat](https://developer.android.com/reference/java/text/NumberFormat)
  + [NumberFormat.Field](https://developer.android.com/reference/java/text/NumberFormat.Field)
  + [ParsePosition](https://developer.android.com/reference/java/text/ParsePosition)
  + [RuleBasedCollator](https://developer.android.com/reference/java/text/RuleBasedCollator)
  + [SimpleDateFormat](https://developer.android.com/reference/java/text/SimpleDateFormat)
  + [StringCharacterIterator](https://developer.android.com/reference/java/text/StringCharacterIterator)
* ## Enums

  + [Normalizer.Form](https://developer.android.com/reference/java/text/Normalizer.Form)
* ## Exceptions

  + [ParseException](https://developer.android.com/reference/java/text/ParseException)
