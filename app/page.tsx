import Image from "next/image";

export default function Home() {
  return (
    <div className="flex items-center justify-center h-screen border-dashed border-2 border-gray-600">
      <h1 className="font-black text-2xl text-blue-400">Panel</h1>
      <p className="mx-4">Enabled</p>
    </div>
  )
}