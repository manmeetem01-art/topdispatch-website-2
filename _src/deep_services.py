# -*- coding: utf-8 -*-
# Deep, page-specific content for each service page.
# keys: why (h2, [paras]), playbook (h2, intro, [(title, text)]), provide [..], kpis [(metric, meaning)],
#       pitfalls (h2, [(title, text)]), extra_faqs [(q,a)]

SD = {
"virtual-receptionist": dict(
 why=("Why the first ring decides who gets the job", [
  "When a homeowner has a problem, they rarely call one company. They search, open two or three listings and dial down the list. The business that answers with a real person, confirms it covers their address and offers a time usually gets the job. Voicemail, a phone tree or a rushed \"can I call you back\" sends the caller to the next number.",
  "Owner-operators and small shops lose these calls for ordinary reasons: the owner is on a ladder, the office manager is on another line, it's lunch, it's 5:05 PM. None of that is visible to the caller. A dedicated virtual receptionist removes the gap between when the phone rings and when someone capable picks it up.",
  "The difference between a virtual receptionist and a basic answering service is what happens after hello. A Top Dispatch receptionist doesn't just take a name and number. They qualify the job, quote from your approved price sheet, book it into your software and tell the customer exactly what happens next, the same way your best office person would."]),
 playbook=("How your receptionist handles a new-customer call", "Every call follows a script you approve. A typical new-customer call runs like this:", [
  ("Greet in your name","\"Thanks for calling Smith Heating and Air, this is Ana. How can I help?\" Callers hear your company, not a call center."),
  ("Confirm the service area","ZIP code or city is checked against your coverage list before anything else, so you never book a job two counties away."),
  ("Understand the problem","Trade-specific questions narrow down what's wrong and how urgent it is. These are written with you during onboarding."),
  ("Quote what you allow","Diagnostic fee, trip charge or flat-rate price from your sheet. Anything custom is passed to you or booked as an estimate."),
  ("Book the slot","The job goes straight into your calendar or field-service software with full notes, address, gate codes and contact details."),
  ("Set expectations","The caller hears the arrival window, what the tech will do first and how they'll be contacted. This one step cuts \"where's my tech?\" callbacks."),
  ("Log and summarise","A short note goes into the CRM and your daily call summary, so you know what came in without listening to recordings.")]),
 provide=["Your greeting and company name as callers should hear it","Services you offer and the ones you don't","Your service area by ZIP code or map","Price sheet: diagnostic fees, trip charges, flat rates, after-hours rates","Which calls should be transferred to you and which should never interrupt you","A user login to your phone system and field-service software"],
 kpis=[("Answer rate","Share of calls answered live during covered hours. The target is close to every call."),("Booking rate","Share of genuine service calls that end with a job on the calendar."),("Average speed to answer","How many rings before a person picks up."),("Transfer rate","How often calls need you personally. This should fall as your receptionist learns the business."),("Callback volume","Customers calling back to ask when the tech is coming. Clear expectations on the first call keep this low.")],
 pitfalls=("Mistakes owners make when they first outsource reception", [
  ("No price guidance","If your receptionist can't quote even a diagnostic fee, callers shop around. Give them the numbers you're comfortable sharing."),
  ("Every call transferred","Forwarding everything back to your cell defeats the purpose. Decide which calls genuinely need you."),
  ("No feedback in week one","The first week is when your receptionist learns your preferences fastest. Read the daily summaries and correct anything small."),
  ("Treating it as message-taking","A trained receptionist can book, quote and dispatch. Using them only to take messages leaves most of the value on the table.")]),
 extra_faqs=[("Can my receptionist answer with my company name?","Yes. They use your exact greeting and company name, so callers experience your office, not an outside service."),("What happens with spam and sales calls?","Your receptionist screens them out and only passes along anything you've said you want to hear about."),("Can I listen to calls?","If your phone system records calls, you can review them any time. Most clients rely on the daily summary instead."),("Can a virtual receptionist work for a one-truck business?","Yes. Part-time coverage of your busiest hours is common for owner-operators who are on jobs all day.")]),

"dispatch": dict(
 why=("Why dispatch is where small shops lose the most money", [
  "Answering the phone gets the job. Dispatch decides whether you make money on it. A poorly routed day means techs driving across town twice, a high-value install waiting behind a filter change, and customers calling to ask where the truck is.",
  "In most small home service businesses, dispatch is done by the owner from the cab of a truck, between jobs, with a phone in one hand. It works until the business has three or four techs. Then schedule clashes, missed close-outs and late arrivals start costing real money and reviews.",
  "A dedicated remote dispatcher keeps the board under control all day. They know which tech is certified for which work, who is closest, which jobs are running long and which customers need a heads-up. You get the benefit of an in-house dispatcher without adding someone to the office payroll."]),
 playbook=("What your dispatcher does through the day", "Dispatch is a running loop, not a single task. Your dispatcher works it continuously:", [
  ("Morning board check","Confirms each tech's first job, flags missing parts or notes and calls the first customers of the day if needed."),
  ("Assign new jobs","New bookings are matched to the right tech by skill, location, workload and your priority rules."),
  ("Send arrival updates","Customers get an on-the-way text or call with a realistic window."),
  ("Handle overruns","When a job runs long, the dispatcher reshuffles later jobs, moves work to another truck and tells affected customers."),
  ("Route emergencies","Urgent calls jump the queue according to your rules, with the nearest qualified tech pulled in."),
  ("Close out","Checks that jobs are marked complete with notes, photos and parts used, so invoicing isn't held up."),
  ("End-of-day summary","Completed, carried-over and follow-up jobs listed for you and tomorrow's board pre-checked.")]),
 provide=["Your technicians, skills, certifications and start/finish times","Territories or zones each tech usually covers","Priority rules: what jumps the queue and what can wait","Your on-call rota and escalation chain","Close-out requirements: photos, notes, signatures, parts","Dispatcher access to your field-service software and team messaging"],
 kpis=[("On-time arrival","Share of jobs where the tech arrives inside the promised window."),("Jobs per tech per day","How full and well-routed each truck's day is."),("Same-day emergency fill","How often urgent calls are reached the same day."),("Close-out completeness","Share of jobs closed with all required notes and photos."),("Customer ETA callbacks","How often customers call asking where the tech is. Good dispatch drives this down.")],
 pitfalls=("Common dispatch problems a dedicated dispatcher fixes", [
  ("Owner as dispatcher","Every reroute interrupts the owner's own job. A dispatcher frees the owner to work or sell."),
  ("No rules for emergencies","Without written rules, urgent calls are handled inconsistently. Your dispatcher works from the rules you approve."),
  ("Silent customers","Customers who aren't told about a delay leave the worst reviews. Your dispatcher keeps them informed."),
  ("Unfinished close-outs","Missing notes delay invoices. Your dispatcher chases them the same day.")]),
 extra_faqs=[("How does a remote dispatcher talk to my techs?","By phone, text and your field-service app, exactly as an in-office dispatcher would."),("Can the dispatcher see where my techs are?","If your software or fleet tracking shows locations, your dispatcher uses it to route jobs."),("What size business needs a dispatcher?","Usually once you have two or more techs and the owner is spending part of every day rearranging the schedule."),("Can you dispatch subcontractors?","Yes, as long as they can receive job details by phone, text or your software.")]),

"after-hours-answering": dict(
 why=("Why after-hours calls are your most valuable calls", [
  "Burst pipes, no-heat calls, lockouts and broken garage springs don't wait for business hours. They're also the calls where customers are least price-sensitive and most likely to book the first company that answers. Sending them to voicemail hands that work to a competitor.",
  "The opposite problem is just as costly: an owner who answers every after-hours call personally is woken at 2 AM for a quote request that could have waited until morning. Over a season that wears people down and leads to missed emergencies anyway.",
  "A trained after-hours receptionist sits between the two. They answer every call live, decide whether it's a real emergency using your rules, page your on-call tech only when it is, and book everything else into the first slot of the next day."]),
 playbook=("How after-hours triage works", "Your receptionist follows a short decision path on every night or weekend call:", [
  ("Answer live","Your company name, a calm voice and a quick question about what's happening."),
  ("Check for safety","Gas smell, sparks, smoke or flooding near electrics trigger your safety script first, including telling the caller to call 911 where appropriate."),
  ("Apply your emergency rules","For example: no heat below 55°F, active leak, no power to the whole home, locked out with a child inside."),
  ("Quote the after-hours fee","Callers hear the emergency rate before a tech is sent, so there are no disputes later."),
  ("Page the on-call tech","With the address, problem and customer contact details. If they don't respond, your escalation chain is followed."),
  ("Book the rest for morning","Non-urgent requests get the first available slot and a confirmation."),
  ("Morning handover","You start the day with a list of everything that came in overnight and what was done.")]),
 provide=["Your written emergency rules and examples","After-hours, weekend and holiday rates","On-call rota with phone numbers and backup contacts","Safety scripts for gas, electrical and flooding calls","Which calls should never be paged overnight","Hours you want covered: evenings, overnight, weekends, holidays"],
 kpis=[("After-hours answer rate","Share of out-of-hours calls answered live."),("Emergency conversion","Share of genuine emergencies that turn into dispatched jobs."),("Unnecessary pages","Overnight pages that turned out not to be urgent. Good triage keeps this near zero."),("Next-morning bookings","Routine requests captured overnight and booked for the day.")],
 pitfalls=("What goes wrong without proper after-hours coverage", [
  ("Voicemail at night","Emergency callers rarely leave messages. They call the next listing."),
  ("Owner burnout","Answering every night call personally isn't sustainable through a peak season."),
  ("No fee disclosure","Sending a tech without quoting the after-hours rate leads to arguments at the door."),
  ("No escalation chain","If the on-call tech is asleep or out of signal, someone else needs to be reached.")]),
 extra_faqs=[("Can you cover just holidays?","Yes. Holiday-only or peak-season coverage can be arranged."),("Will my customers know it's after-hours coverage?","They hear your company name and a trained person. Most can't tell it isn't your office."),("Do you charge more for overnight shifts?","Pricing depends on the hours covered. Tell us your schedule and we quote a flat monthly fee."),("Can after-hours calls be booked into my software?","Yes. Your receptionist books routine work directly into your calendar or field-service software.")]),

"appointment-setting": dict(
 why=("Why a full calendar depends on follow-up, not just answering", [
  "Most home service businesses already generate more interest than they convert. Estimates go out and are never chased. Maintenance customers forget their annual visit. Tomorrow's jobs aren't confirmed, so techs arrive at empty houses.",
  "Each of those gaps is small on its own. Together they leave revenue sitting in your CRM. An appointment setter's job is to close them every day: book what comes in, confirm what's scheduled, and call back what's still open.",
  "Because the same person handles your inbound calls and your follow-ups, they know which customers already spoke to you, what was quoted and what the hesitation was. That context makes follow-up calls feel like service, not sales."]),
 playbook=("The daily appointment-setting routine", "A typical day for your appointment setter:", [
  ("Book inbound requests","Every call or web lead gets a slot, not a callback promise."),
  ("Confirm tomorrow","Each job on tomorrow's board is confirmed by call or text, with gate codes and access checked."),
  ("Refill cancellations","Freed slots are offered to waitlisted customers or emergency calls."),
  ("Work open estimates","Estimates older than your chosen number of days get a friendly follow-up call."),
  ("Book maintenance","Customers due for annual or seasonal service are contacted and scheduled."),
  ("Update the CRM","Every outcome is logged so nothing is called twice or forgotten.")]),
 provide=["Job types and how long each takes","Booking rules: buffers, territories, slots held for emergencies","Your estimate follow-up timing and what to say","Maintenance plan terms and which customers are due","Calendar or field-service software access","Approved text templates for confirmations and reminders"],
 kpis=[("Booking rate","Share of inbound requests that end in a scheduled job."),("No-show rate","Jobs where the customer wasn't home. Day-before confirmation reduces this."),("Estimate close rate","Share of open estimates that convert after follow-up."),("Maintenance renewal rate","Share of due customers who book their next visit.")],
 pitfalls=("Where calendars leak", [
  ("Unconfirmed jobs","A wasted trip costs fuel, time and a slot another customer wanted."),
  ("Estimates left to chance","Customers who don't hear back often assume you're too busy."),
  ("No waitlist","Cancellations become dead time instead of booked work."),
  ("Follow-up only when slow","Consistent follow-up every week beats bursts when the board looks empty.")]),
 extra_faqs=[("Can you book from web form leads?","Yes. Leads from your website or ads can be called and booked within minutes during covered hours."),("Do you send text reminders?","Your setter sends reminders through your software or phone system using templates you approve."),("Can you handle multiple calendars?","Yes, including separate calendars for techs, estimators and crews."),("How fast do you call web leads?","During covered hours, new leads are called as soon as they arrive.")]),

"cold-calling": dict(
 why=("Why outbound calling works best on warm lists", [
  "For home service companies, the most profitable outbound calls usually aren't to strangers. They're to past customers due for service, members whose maintenance plan lapsed, homeowners who got an estimate and went quiet, and property managers who need a reliable vendor.",
  "These people already know your name. A friendly, well-timed call reminds them and makes booking easy. That's why a dedicated caller working your own lists tends to outperform purchased lead lists and generic telemarketing.",
  "Top Dispatch callers work from scripts you approve, log every outcome in your CRM and report weekly, so you can see exactly which lists and offers are producing booked visits."]),
 playbook=("How an outbound campaign runs", "Each campaign follows the same structure:", [
  ("Choose the list","Past customers, lapsed plans, open estimates, commercial prospects or a new neighbourhood."),
  ("Agree the offer","A seasonal tune-up, a plan renewal, a free inspection or a commercial walkthrough."),
  ("Write the script together","Opening line, two or three qualifying questions and a clear booking ask."),
  ("Call in daily blocks","Consistent daily calling, with callbacks scheduled for people who ask."),
  ("Book or qualify","Interested contacts are booked straight into your calendar or handed to sales with notes."),
  ("Report weekly","Dials, conversations, bookings and feedback, with suggestions for the next week.")]),
 provide=["The lists you're entitled to contact","Your offer and pricing for the campaign","Who should receive qualified leads","Any do-not-call or opt-out records","Compliance rules for your state and industry","CRM access for logging outcomes"],
 kpis=[("Contact rate","Share of dials that reach a person."),("Conversation-to-booking rate","Share of conversations that end in a booked visit."),("Bookings per week","The number that matters most for your pipeline."),("Show rate","Share of booked outbound visits that actually happen.")],
 pitfalls=("What makes outbound calling fail", [
  ("Cold purchased lists","Strangers convert far worse than your own past customers."),
  ("No clear offer","\"Just checking in\" calls rarely book. A specific reason to book does."),
  ("Ignoring compliance","Outbound calling is regulated. Work only from lists you can contact and follow opt-outs."),
  ("No tracking","Without weekly numbers you can't tell which lists are worth calling.")]),
 extra_faqs=[("Can you call commercial property managers?","Yes. B2B prospecting for property managers, HOAs and facilities teams is common for trades."),("Do you use auto-dialers?","Calls are made by your dedicated caller. We follow your compliance requirements on dialing methods."),("How many calls a day can one caller make?","It depends on list quality and script length. Your weekly report shows actual activity."),("Can outbound and inbound be combined?","Yes. Many clients schedule outbound blocks around quieter inbound hours.")]),

"back-office-support": dict(
 why=("Why admin backlog costs more than it looks", [
  "Admin rarely feels urgent until it is. Invoices that go out a week late get paid a month late. A messy CRM means duplicate customers, missed maintenance reminders and unreliable reports. An unanswered inbox means suppliers, insurers and customers waiting.",
  "In most small trade businesses, this work lands on the owner in the evening or on a partner at weekends. It's the least valuable use of the most valuable person's time.",
  "A remote back-office assistant clears it during your working day. Because they often also answer your phones, they already know the jobs, the customers and what was agreed, which makes the admin faster and more accurate."]),
 playbook=("A typical back-office week", "Your assistant works through a recurring list you agree together:", [
  ("Daily invoicing","Completed jobs are checked against notes and invoiced the same or next day."),
  ("Collections","Overdue invoices get polite reminder emails and calls on your schedule."),
  ("Inbox","Shared inbox triaged daily: answered, filed or flagged for you."),
  ("CRM upkeep","Duplicates merged, contact details corrected, job histories completed."),
  ("Estimates and documents","Quotes, proposals, permits, warranty claims and supplier forms prepared."),
  ("Reviews","Happy customers sent review requests after completed jobs.")]),
 provide=["The tasks that currently pile up","Access to your invoicing tool, CRM and shared inbox","Your payment terms and reminder wording","Templates for estimates and common emails","Who approves anything financial","A short list of things that always need your sign-off"],
 kpis=[("Days to invoice","Time from job completion to invoice sent."),("Overdue balance","Value of invoices past due, tracked weekly."),("Inbox response time","How quickly customer and supplier emails get a reply."),("CRM data quality","Duplicates and missing fields, checked monthly.")],
 pitfalls=("Back-office mistakes we see most", [
  ("Batching invoices weekly","Late invoices mean late payment. Daily invoicing improves cash flow."),
  ("Too much access","Give your assistant only the tools the work needs. Payments and banking stay with you."),
  ("No templates","Templates make work consistent and quicker to review."),
  ("Nobody owns the CRM","Data decays fast without a person responsible for it.")]),
 extra_faqs=[("Can you work in QuickBooks?","Yes, for invoicing and record-keeping tasks you assign. Payments and approvals stay with you."),("Do you do bookkeeping?","We handle admin such as invoicing, data entry and reminders. Accounting and tax work should stay with your accountant."),("Can you prepare permit applications?","Yes, using information you provide, for you to review and submit."),("Is back office available part-time?","Yes, and it's often combined with phone coverage in one role.")]),

"reporting-analytics": dict(
 why=("Why most owners don't know their numbers, and why it matters", [
  "Field-service software is full of data, but pulling it into something useful takes time few owners have. As a result, decisions about hiring, marketing and pricing are often made on gut feel.",
  "A short, consistent weekly report changes that. When you see calls, bookings, completed jobs, average ticket and open estimates every Monday, problems show up early: a marketing channel that stopped producing, a tech whose callbacks are rising, or estimates that are going cold.",
  "Your Top Dispatch assistant builds that report from the tools you already use and sends it on the same day every week, so the numbers become a habit rather than a project."]),
 playbook=("What goes into a weekly operations report", "We build the report around the decisions you actually make:", [
  ("Calls","Total calls, answered live, missed and booked, by day."),
  ("Bookings by source","Google, referrals, repeat customers, ads or outbound."),
  ("Jobs completed","Per tech, with average ticket where available."),
  ("Open estimates","Number and value, with the oldest flagged for follow-up."),
  ("Cancellations and callbacks","What was lost and why, when the reason is known."),
  ("Three things to look at","A short note on anything unusual that week.")]),
 provide=["The five to ten numbers you want to track","Access to your phone system and field-service reports","Your preferred format: email, sheet or dashboard","Who should receive the report","Any targets you want progress shown against"],
 kpis=[("Report on time","Delivered on the agreed day, every week."),("Data accuracy","Numbers reconcile with your software."),("Actions taken","Flagged items followed up the same week.")],
 pitfalls=("Reporting traps to avoid", [
  ("Too many metrics","A report nobody reads is worse than none. Start small."),
  ("Inconsistent timing","Weekly numbers only help if they arrive weekly."),
  ("Messy source data","Clean CRM records first, or the report will mislead you."),
  ("No owner for follow-up","Each flagged item needs a person and a deadline.")]),
 extra_faqs=[("Can reports include marketing spend?","Yes, if you share spend figures, reports can show cost per booked job by channel."),("Can I get a dashboard instead of a PDF?","Yes. We can maintain a shared spreadsheet or the dashboard in your existing tools."),("How long until the first report?","Usually within the first two weeks, once access and metrics are agreed."),("Is reporting available on its own?","It's usually added to a receptionist or back-office role, which keeps cost down.")]),

"customer-support": dict(
 why=("Why support after the job drives reviews and repeat work", [
  "For home service businesses, online reviews are often the deciding factor between you and the next listing. Most unhappy customers don't complain to you first. They post. Most happy ones never think to leave a review unless asked.",
  "Customer support after the job addresses both. A quick check-in call catches problems while they can still be fixed. A timely review request turns satisfied customers into public proof.",
  "Your Top Dispatch support specialist handles questions, complaints and follow-ups by phone and email, using the tone and limits you set, and logs everything so your team learns from it."]),
 playbook=("How complaints and follow-ups are handled", "Each support contact follows a consistent approach:", [
  ("Listen first","Let the customer explain fully and confirm the details back."),
  ("Check the job record","Pull notes, photos and invoice from your software."),
  ("Resolve within limits","Offer what you've authorised, such as a revisit or a goodwill gesture."),
  ("Escalate the rest","Anything beyond the limits goes to you with a clear summary."),
  ("Close the loop","Customer told what happens next and when."),
  ("Ask for a review","Customers who are happy with the outcome receive a review link, in line with platform rules.")]),
 provide=["Your service guarantee and warranty terms","What support can offer without asking you","Escalation contacts and response times","Review platforms you want to grow","Tone guidelines and phrases to avoid","Access to job records and shared inbox"],
 kpis=[("Complaint resolution time","Hours from first contact to resolution."),("Reviews requested","Review links sent after completed jobs."),("Review rating trend","Average rating over time on your main platforms."),("Repeat booking rate","Customers who book again after a support contact.")],
 pitfalls=("Support habits that hurt reputation", [
  ("Slow replies","A complaint left overnight often becomes a one-star review."),
  ("Defensive tone","Customers want to be heard before they hear explanations."),
  ("Asking selectively","Platforms discourage review gating. Follow their rules when requesting reviews."),
  ("No record","Patterns in complaints are only visible when every contact is logged.")]),
 extra_faqs=[("Can you reply to Google reviews?","We draft replies for your approval, or post under your guidelines if you prefer."),("Do you handle warranty claims?","Yes. We log the claim, check terms and schedule a revisit within the rules you set."),("Can support work in Spanish?","Tell us if you need bilingual support and we'll check availability for your match."),("Is customer support separate from reception?","It can be combined in the same role, which is common for smaller businesses.")]),
}
