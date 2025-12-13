"use client";
import React from 'react'
import AuthTokenLogger from '@/components/AuthTokenLogger'

type Props = {
  children: React.ReactNode
}

const AuthLayout = ({children}: Props) => {
  return (
    <div className="flex justify-center pt-10">
      <AuthTokenLogger />
      {children}
    </div>
  )
}

export default AuthLayout