import java
import semmle.code.java.frameworks.android.Intent
import TestUtilities.InlineFlowTest

class SummaryModelTest extends SummaryModelCsv {
  override predicate row(string row) {
    row =
      [
        //"package;type;overrides;name;signature;ext;inputspec;outputspec;kind",
        "generatedtest;Test;false;getMapKeyDefault;(Bundle);;MapKey of Argument[0];ReturnValue;value"
      ]
  }
}
