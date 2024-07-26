export default function (mathFunction) {
  const queue = [];
  try { queue.push(mathFunction()); } finally {
    queue.push('Guardrail was processed');
  } return queue;
}
