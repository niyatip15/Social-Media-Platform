<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-right">
            <!-- Centering Container -->
            <div class="flex justify-center items-center h-screen">
                <div class="p-12 bg-white border border-gray-200 rounded-lg w-full max-w-md">
                    <!-- Signup Heading -->
                    <h2 class="text-2xl font-bold mb-6">Sign Up</h2>
                    <form class="space-y-6">
                        <div>
                            <label>Name</label><br>
                            <input type="text" placeholder="Your full name" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        </div>

                        <div>
                            <label>E-mail</label><br>
                            <input type="email" placeholder="Your e-mail address" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        </div>

                        <div>
                            <label>Password</label><br>
                            <input type="password" placeholder="Your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        </div>

                        <div>
                            <label>Repeat password</label><br>
                            <input type="password" placeholder="Repeat your password" class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                        </div>

                        <div>
                            <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign up</button>
                        </div>
                    </form>
                     <p class="font-bold">
                        have an account? <RouterLink :to="{'name': 'login'}" class="underline">Click here</RouterLink> to Login!
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>
