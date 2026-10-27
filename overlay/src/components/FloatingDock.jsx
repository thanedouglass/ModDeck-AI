import { useEffect, useMemo, useState } from 'react'

import QueueItem from './QueueItem'

export default function FloatingDock() {
  const [queue, setQueue] = useState([])

  useEffect(() => {
    let cancelled = false

    const fetchQueue = async () => {
      try {
        const response = await fetch('/api/queue')
        if (!response.ok) {
          return
        }

        const data = await response.json()
        if (!cancelled && Array.isArray(data)) {
          setQueue(data)
        }
      } catch {
        // Keep previous state if polling fails.
      }
    }

    fetchQueue()
    const interval = setInterval(fetchQueue, 1000)

    return () => {
      cancelled = true
      clearInterval(interval)
    }
  }, [])

  const active = queue[0]
  const upcoming = useMemo(() => queue.slice(1, 4), [queue])

  return (
    <section className="h-[180px] w-[320px] backdrop-blur-md bg-slate-900/80 border border-slate-700/50 rounded-xl p-3 shadow-2xl text-white">
      <p className="text-[10px] uppercase tracking-wide text-slate-400">ModDeck-AI Live Queue</p>
      <div className="mt-2 rounded-lg border border-slate-700/50 bg-slate-800/50 p-2">
        <p className="text-[10px] text-slate-400">Active track/action</p>
        <p className="mt-1 truncate text-sm font-semibold text-white">
          {active?.song_or_action ?? 'Waiting for community picks...'}
        </p>
        <p className="truncate text-xs text-slate-400">{active?.user ? `by ${active.user}` : ''}</p>
      </div>

      <div className="mt-2">
        <p className="mb-1 text-[10px] uppercase tracking-wide text-slate-400">Up next</p>
        <ul className="space-y-1">
          {upcoming.length === 0 ? (
            <li className="rounded-md bg-slate-800/50 px-2 py-1 text-xs text-slate-400">No queued picks.</li>
          ) : (
            upcoming.map((item) => <QueueItem key={item.id} item={item} />)
          )}
        </ul>
      </div>
    </section>
  )
}
