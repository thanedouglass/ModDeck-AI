export default function QueueItem({ item }) {
  return (
    <li className="flex items-center justify-between rounded-md bg-slate-800/70 px-2 py-1 text-xs">
      <span className="truncate pr-2">
        <span className="font-semibold text-slate-200">{item.user}</span>
        <span className="text-slate-400"> · </span>
        <span className="text-slate-300">{item.song_or_action}</span>
      </span>
      {item.is_mod_approved ? (
        <span className="rounded bg-emerald-500/20 px-1.5 py-0.5 text-[10px] font-semibold text-emerald-300">
          mod-approved
        </span>
      ) : null}
    </li>
  )
}
