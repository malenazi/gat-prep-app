export function nowMs(): number {
  return Date.now();
}

export function todayIsoDate(): string {
  return new Date().toISOString().split('T')[0];
}
