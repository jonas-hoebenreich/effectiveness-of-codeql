/**
 * For internal use only.
 *
 * @name NoSQL database query built from user-controlled sources (boosted)
 * @description Building a database query from user-controlled sources is vulnerable to insertion of
 *              malicious code by the user.
 * @kind path-problem
 * @scored
 * @problem.severity error
 * @security-severity 8.8
 * @id adaptive-threat-modeling/js/nosql-injection
 * @tags experimental experimental/atm security
 */

import ATM::ResultsInfo
import DataFlow::PathGraph
import experimental.adaptivethreatmodeling.NosqlInjectionATM

from
  DataFlow::Configuration cfg, DataFlow::PathNode source, DataFlow::PathNode sink, float score,
  string scoreString
where
  cfg.hasFlowPath(source, sink) and
  not isFlowLikelyInBaseQuery(source.getNode(), sink.getNode()) and
  score = getScoreForFlow(source.getNode(), sink.getNode()) and
  scoreString = getScoreStringForFlow(source.getNode(), sink.getNode())
select sink.getNode(), source, sink,
  "[Score = " + scoreString + "] This may be a NoSQL query depending on $@ " +
    getAdditionalAlertInfo(source.getNode(), sink.getNode()), source.getNode(),
  "a user-provided value", score
