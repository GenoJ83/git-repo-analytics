function rankContributors(commits) {
  const counts = {};
  for (const c of commits) {
    counts[c.author] = (counts[c.author] || 0) + 1;
  }
  return Object.entries(counts).sort((a, b) => b[1] - a[1]);
}
function totalChurn(insertions, deletions) {
  return insertions + deletions;
}
module.exports = { rankContributors, totalChurn };
